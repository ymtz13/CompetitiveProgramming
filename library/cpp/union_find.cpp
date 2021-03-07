#include<iostream>
#include<vector>
using namespace std;
#define ll long long

class UF{
public:
  vector<ll> uf;
  ll n;
  
  UF(ll N): uf(N, -1), n(N) {}

  ll find(ll x){
    if(uf[x]<0) return x;
    return uf[x] = find(uf[x]);
  }

  ll size(ll x){ return -uf[find(x)]; }

  void connect(ll x, ll y){
    x = find(x); y = find(y);
    if(x==y) return;
    if (size(x)>size(y)) { ll c=x; x=y; y=c; }
    uf[y] += uf[x];
    uf[x] = y;
    --n;
  }

};

int main(){
  UF uf(100);
  cout << uf.find(0) << endl;
  uf.connect(0,5);
  uf.connect(0,8);
  uf.connect(8,10);
  cout << uf.find(0) << endl;
  cout << uf.size(0) << endl;
  cout << uf.n << endl;

  return 0;
}
