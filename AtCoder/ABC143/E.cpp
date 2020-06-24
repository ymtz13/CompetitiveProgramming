#include<iostream>
#include<vector>
#include<set>
#include<algorithm>
using namespace std;
#define ll long long

int main(){
  ll N, M, L;
  cin >> N >> M >> L;
  ll d[N][N];
  vector<vector<ll>> e;
  vector<vector<ll>> reachable_1shot;
  for(ll i=0; i<N; ++i){
    for(ll j=0; j<N; ++j) d[i][j] = 10e10;
    vector<ll> dummy;
    e.push_back(dummy);
    reachable_1shot.push_back(dummy);
  }

  ll A, B, C;
  for(ll i=0; i<M; ++i){
    cin >> A >> B >> C;
    d[A-1][B-1] = C;
    d[B-1][A-1] = C;
    e[A-1].push_back(B-1);
    e[B-1].push_back(A-1);
  }
  
  for(ll st=0; st<N; ++st){
    vector<ll> fuel_remain(N, -1);
    fuel_remain[st] = L;
    set<ll> nodes;
    nodes.insert(st);

    //cout << "st" << st<<endl;
    
    while(nodes.size()>0){
      set<ll> nodes_new;
      for(auto itr_from = nodes.begin(); itr_from!=nodes.end(); ++itr_from) {
        vector<ll> edges = e[*itr_from];
        for(auto itr_to = edges.begin(); itr_to!=edges.end(); ++itr_to){
          //cout << (*itr_from) << "-" << (*itr_to) << endl;
          ll fuel_remain_new = fuel_remain[*itr_from]-d[*itr_from][*itr_to];
          if(fuel_remain_new > fuel_remain[*itr_to]){
            fuel_remain[*itr_to] = fuel_remain_new;
            nodes_new.insert(*itr_to);
            //cout << (*itr_to) << "is reachable with fuel_remain "<< fuel_remain_new << endl;
          }
        }
      }
      nodes = nodes_new;
    }

    for(ll goal=0; goal<N; ++goal){
      if(fuel_remain[goal]>=0 && goal!=st) { reachable_1shot[st].push_back(goal); }
    }
  }

  /*for(ll st=0; st<N; ++st){
    cout << "st->"<<st <<"    "  ;
    for(ll i=0; i<reachable_1shot[st].size(); ++i) cout << reachable_1shot[st][i] << " ";
    cout<<endl;
    }*/

  ll Q;
  cin >> Q;
  for(ll i=0; i<Q; ++i){
    ll s,t;
    cin >> s >> t;
    set<ll> nodes_reach;
    set<ll> nodes;
    nodes_reach.insert(s-1);
    nodes.insert(s-1);
    ll k;
    for(k=0; k<N+1 && nodes.size()>0 && nodes.find(t-1)==nodes.end(); ++k){
      //cout <<endl<<"turn" << k <<endl;
      
      set<ll> nodes_new;
      for(auto itr_from = nodes.begin(); itr_from!=nodes.end(); ++itr_from) {
        vector<ll> edges = reachable_1shot[*itr_from];
        for(auto itr_to = edges.begin(); itr_to!=edges.end(); ++itr_to) {
          //cout << (*itr_from) << "-" << (*itr_to) << endl;
          if( nodes_reach.find(*itr_to)==nodes_reach.end() ){
            nodes_reach.insert(*itr_to);
            nodes_new.insert(*itr_to);
            //cout << (*itr_to) << "is reached"<< endl;
          }
        }
      }
      nodes = nodes_new;
    }

    if( nodes_reach.find(t-1)!=nodes_reach.end() ){
      cout << k-1 << endl;
    }else{
      cout << -1 << endl;
    }

  }
  

  return 0;
}
