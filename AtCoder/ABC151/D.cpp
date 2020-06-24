#include<iostream>
#include<vector>
using namespace std;
#define ll long long

int main(){
  ll H,W;
  cin >> H >> W;
  vector<ll> row(W+2, -1);
  vector<vector<ll>> M(H+2, row);
  vector<vector<ll>> X;
  
  for(ll h=0; h<H; ++h) {
    string s;
    cin >> s;
    for(ll w=0; w<W; ++w) {
      if(s[w]=='#') continue;
      M[h+1][w+1] = 0;
      vector<ll> x = {h+1, w+1};
      X.push_back(x);
    }
  }

  //for(ll h=0; h<H+2; ++h) {
  //for(ll w=0; w<W+2; ++w)
  //  cout << -M[h][w]; cout << endl;}


  ll mark = 0, ans = 0;
  for(ll ist=0    ; ist<X.size(); ++ist)  { 
    ++mark;
    ll turn = 0;
    bool f = false;
    vector<vector<ll>> queue = {X[ist]};
    M[X[ist][0]][X[ist][1]] = mark;

    while(queue.size() && !f) {
      vector<vector<ll>> queue_new;
      for(ll iq=0; iq<queue.size(); ++iq) {
        ll qx = queue[iq][0], qy = queue[iq][1];
        
        //cout << ist << ":" << turn << ":" << qx << "," <<  qy << endl;
        
        ll x, y, m;
        x = qx+1; y = qy  ; m = M[x][y];
        if(m!=-1 && m!=mark) { M[x][y] = mark; vector<ll> xx = {x,y}; queue_new.push_back(xx); }
        x = qx-1; y = qy  ; m = M[x][y];
        if(m!=-1 && m!=mark) { M[x][y] = mark; vector<ll> xx = {x,y}; queue_new.push_back(xx); }
        x = qx  ; y = qy+1; m = M[x][y];
        if(m!=-1 && m!=mark) { M[x][y] = mark; vector<ll> xx = {x,y}; queue_new.push_back(xx); }
        x = qx  ; y = qy-1; m = M[x][y];
        if(m!=-1 && m!=mark) { M[x][y] = mark; vector<ll> xx = {x,y}; queue_new.push_back(xx); }
        
      }

      queue = queue_new;
      ++turn;
    }

    ans = max(ans, turn-1);

  }

  cout << ans << endl;

  return 0;
}
