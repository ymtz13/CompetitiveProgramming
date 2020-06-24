#include<iostream>
#include<set>
#include<vector>
using namespace std;
#define ll long long

class P {
public:
  ll L, R, C;
  P(ll _L, ll _R, ll _C): L(_L),R(_R),C(_C) {}
};

struct cmp_L { bool operator()(const P x, const P y) const { return x.L < y.L; } } Cmp_L;
struct cmp_R { bool operator()(const P x, const P y) const { return x.R < y.R; } } Cmp_R;
struct cmp_C { bool operator()(const P x, const P y) const { return x.C < y.C; } } Cmp_C;

int main(){
  ll N, M;
  cin >> N >> M;

  multiset<P, cmp_L> Plist;
  multiset<P, cmp_C> Qlist;
  for(ll m=0; m<M; ++m) {
    ll L, R, C;
    cin >> L >> R >> C;
    P p(L,R,C);
    Plist.insert(p);
  }

  for(auto ip=Plist.begin(); ip!=Plist.end(); ++ip) { cout << (ip->L) << "," << (ip->R) << "," << (ip->C) << " "; } cout << endl;

  ll i=1;
  vector<ll> D(N+1);
  D[1]=0;

  while(i<N){
    {
      auto ip = Plist.begin();
      for(; ip!=Plist.end() && (ip->L)<=i; ++ip){
        P q(*ip);
        q.C += D[q.L];
        Qlist.insert(q);
      }
      Plist.erase(Plist.begin(), ip);
    }

    for(auto ip=Plist.begin(); ip!=Plist.end(); ++ip) { cout << (ip->L) << "," << (ip->R) << "," << (ip->C) << " "; } cout << " P" << endl;
    for(auto ip=Qlist.begin(); ip!=Qlist.end(); ++ip) { cout << (ip->L) << "," << (ip->R) << "," << (ip->C) << " "; } cout << " Q" << endl;

    for(auto itr = Qlist.begin(); itr!=Qlist.end(); ++itr){
      if(itr->R>i) break;
      Qlist.erase(itr);
    }

    if(Qlist.size()==0){ cout << -1 << endl; return 0; }
    
    auto qq = Qlist.begin();
    for(ll r=i+1; r<qq->R+1; ++r){
      D[r] = qq->C;
    }
    i = qq->R;
  }

  cout << D[N]<<endl;

  return 0;
}
