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
  ll N;
  cin >> N;

  ll ans = 0;
  for(ll n=1; n<=N; n+=2) {
    map<ll, ll> f = factorize(n);
    ll d=1;
    for(auto itr=f.begin(); itr!=f.end(); ++itr) d*=(1+itr->second);
    if(d==8) ++ans;
  }

  cout << ans << endl;
  
  return 0;
}
