#include<iostream>
#include<vector>
#include<algorithm>
#include<map>
using namespace std;
#define ll long long

vector<vector<ll>> e_input;
vector<vector<ll>> e;
map<vector<ll>, ll> ie;
ll max_color = -1;

void dfs(ll par, ll i, ll color_par) {
  ll color = 0;
  for(ll j=0; j<e[i].size(); ++j) {
    if (e[i][j]==par) continue;
    if (color==color_par) {++color;}
    vector<ll> _e = {i, e[i][j]};
    sort(_e.begin(), _e.end());
    ie[_e] = color;
    dfs(i, e[i][j], color);
    ++color;
  }
  max_color = max(max_color, color-1);

}

int main(){
  ll N;
  cin >> N;
  e.resize(N);
  for(ll i=0; i<N-1; ++i){
    ll a,b;
    cin >> a >> b;

    vector<ll> e_inp = {a-1, b-1};
    sort(e_inp.begin(), e_inp.end());
    e_input.push_back(e_inp);

    e[a-1].emplace_back(b-1);
    e[b-1].emplace_back(a-1);
  }
  
  dfs(-1, 0, -1);

  cout << max_color+1 << endl;
  for(ll i=0; i<e_input.size(); ++i){
    cout << ie[e_input[i]]+1 << endl;
  }
  
  return 0;
}
