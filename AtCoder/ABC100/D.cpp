#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
#define ll long long

struct C {
  ll x, y, z;
  C(ll x, ll y ,ll z) : x(x), y(y), z(z) {}
};

int main(){
  ll N, M;
  cin >> N >> M;

  vector<C> cakes;
  for(ll i=0; i<N; ++i) {
    ll x, y, z;
    cin >> x >> y >> z;
    cakes.emplace_back(x,y,z);
  }
  
  ll ans=0;
  vector<ll> v(N);

  for(ll sx=-1; sx<=1; sx+=2)
  for(ll sy=-1; sy<=1; sy+=2)
  for(ll sz=-1; sz<=1; sz+=2) {
    for(ll i=0; i<N; ++i) {
      C& c = cakes[i];
      v[i] = c.x*sx + c.y*sy + c.z*sz;
    }
    sort(v.begin(), v.end());
    ll sum = 0;
    for(ll i=0; i<M; ++i) sum += v[N-1-i];
    if(ans<sum) ans = sum;
  }

  cout << ans << endl;

  return 0;
}
