#include<iostream>
#include<map>
using namespace std;
#define ll long long

ll gcd(ll a, ll b) {
  ll c;
  if (a>b) { c=a; a=b; b=c; }
  while(a>0) { c=a; a=b%a; b=c; }
  return b;
}

map<ll, ll> factorize(ll a) {
  map<ll, ll> factors;
  ll v = a;
  for(ll p=2; p*p<=a; ++p){
    if(v%p==0) factors[p]=0;
    while(v%p==0) { v/=p; ++factors[p]; }
  }
  if(v>1) factors[v]=1;
  return factors;
}


int main(){
  ll x, y;
  cin >> x >> y;
  cout << x << "," << y << "," << gcd(x,y) << endl;

  auto factors = factorize(x);
  for(auto itr = factors.begin(); itr!=factors.end(); ++itr) {
    cout << (itr->first) << ":" << (itr->second) << endl;
  }
  return 0;
}
