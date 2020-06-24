#include<iostream>
#include<vector>
#include<set>
using namespace std;
#define ll long long

int main(){
  ll N;
  cin >> N;
  
  ll S[N][N];
  vector<ll> E[N];
  for(ll i=0; i<N; ++i){
    string s;
    cin >> s;    
    for(ll j=0; j<N; ++j) {
      S[i][j] = s[j]=='1' ? 1 : 0;
      if(S[i][j]==1) { E[i].emplace_back(j); }
    }
  }

  // for(ll i=0; i<N; ++i){
  //   for(ll j=0; j<N; ++j) cout << S[i][j] << " ";
  //   cout << endl;
  // }
  // for(ll i=0; i<N; ++i){
  //   for(auto itr = E[i].begin(); itr!=E[i].end(); ++itr) cout << (*itr) << " ";
  //   cout << endl;
  // }

  ll max_size = -1;
  ll dist[N];
  for(ll start=0; start<N; ++start){
    for(int i=0; i<N; ++i) dist[i]=-1;
    dist[start]=0;
    set<ll> queue = {start};
    ll d=1;
    ll conflict=0;
    
    while(queue.size()>0 && conflict==0){
      set<ll> queue_new;
      for(auto itr_par=queue.begin(); itr_par!=queue.end(); ++itr_par){
        vector<ll>& edge = E[*itr_par];
        for(auto itr_chi = edge.begin(); itr_chi!=edge.end(); ++itr_chi){
          
          if(dist[*itr_chi]==dist[*itr_par]){ conflict=1; break; }
          if(dist[*itr_chi]==-1){
            dist[*itr_chi]=d;
            queue_new.emplace(*itr_chi);
          }
        }
        if(conflict==1) break;
      }
      queue = queue_new;
      ++d;
    }

    if(conflict==0) max_size = max(d, max_size);
    
  }

  cout << (max_size==-1? -1:  max_size-1) << endl;

  return 0;
}
