#include<iostream>
#include<vector>
#include<set>
using namespace std;
#define ll long long

int main(){
  ll H, W;
  cin >> H >> W;
  vector<vector<ll>> M(H);
  vector<vector<set<ll>>> P(H);
  vector<vector<set<ll>>> Q(H);
  for(ll h=0; h<H; ++h){
    vector<ll> row(W);
    for(ll w=0; w<W; ++w){
      cin >> row[w];
    }
    M[h] = row;

    vector<set<ll>> prow(W);
    P[h] = prow;
    Q[h] = prow;
  }
  for(ll h=0; h<H; ++h){
    for(ll w=0; w<W; ++w){
      ll B;
      cin >> B;
      M[h][w] = abs(M[h][w]-B);
    }
  }

  /*
  for(ll h=0; h<H; ++h){
    for(ll w=0; w<W; ++w) cout << M[h][w] << " "; cout<<endl;
  }
  */

  ll L = (H+W+1)/2;

  P[0][0].insert(M[0][0]);
  for(ll h=0; h<H; ++h){
    for(ll w=0; w+h+1<=L; ++w){
      set<ll>& pn = P[h][w];
      ll vn = M[h][w];

      if(h>0){
        set<ll>& pp = P[h-1][w];
        for(auto itr=pp.begin(); itr!=pp.end(); ++itr) {
          ll vp=(*itr);
          pn.insert(vp+vn);
          pn.insert(abs(vp-vn));
        }
      }
      
      if(w>0) {
        set<ll>& pp = P[h][w-1];
        for(auto itr=pp.begin(); itr!=pp.end(); ++itr) {
          ll vp=(*itr);
          pn.insert(vp+vn);
          pn.insert(abs(vp-vn));
        }
      }
    }
  }

  Q[H-1][W-1].insert(M[H-1][W-1]);
  for(ll h=H-1; h>=0; --h){
    for(ll w=W-1; w+h+1>=L; --w){
      set<ll>& pn = Q[h][w];
      ll vn = M[h][w];

      if(h<H-1){
        set<ll>& pp = Q[h+1][w];
        for(auto itr=pp.begin(); itr!=pp.end(); ++itr) {
          ll vp=(*itr);
          pn.insert(vp+vn);
          pn.insert(abs(vp-vn));
        }
      }
      
      if(w<W-1) {
        set<ll>& pp = Q[h][w+1];
        for(auto itr=pp.begin(); itr!=pp.end(); ++itr) {
          ll vp=(*itr);
          pn.insert(vp+vn);
          pn.insert(abs(vp-vn));
        }
      }
    }
  }

  ll ans = 10000000;
  for(ll h=0; h<H; ++h){
    for(ll w=0; w<W; ++w){
      if(h+w+1!=L) continue;

      auto ip = P[h][w].begin();
      auto iq = Q[h][w].begin();
      while(ip!=P[h][w].end() && iq!=Q[h][w].end()){
        ans = min(ans, abs((*ip)-(*iq)));
        if((*ip)<(*iq)){ip++;}else{iq++;}
      }
    }
  }
    
  cout << ans << endl;
  return 0;
}
