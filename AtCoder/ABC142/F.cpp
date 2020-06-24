#include<iostream>
#include<vector>
using namespace std;
#define ll long long

vector<vector<ll>> from;
vector<ll> seikai;

void visit(ll st, ll n, vector<ll> keiro){
  keiro.emplace_back(n);
  for(ll i=0; i<from[n].size(); ++i){
    if(st==from[n][i]){ seikai=keiro; break; }
    visit(st, from[n][i], keiro);
  }
  keiro.pop_back();
}


int main(){
  ll N, M;
  cin >> N >> M;
  
  vector<vector<ll>> from_(N);
  from = from_;
  vector<vector<ll>> to(N);
  for(ll m=0; m<M; ++m){
    ll A, B;
    cin >> A >> B;
    from[A-1].emplace_back(B-1);
    to  [B-1].emplace_back(A-1);
  }

  
  for(ll n=0; n<N; ++n){
    vector<ll> keiro;
    visit(n, n, keiro);
    if(seikai.size()>0) break;
  }

  cout << seikai.size() << endl;;
  for(ll i=0; i<seikai.size(); ++i ){
    cout << seikai[i]+1  << endl;
  }
  
  return 0;
}
