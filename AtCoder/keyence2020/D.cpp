#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
#define ll long long

int main(){
  ll N;
  cin >> N;

  vector<ll> A(N), B(N);
  for(ll i=0; i<N; ++i) cin >> A[i];
  for(ll i=0; i<N; ++i) cin >> B[i];

  ll ans = 1e10;
  ll pos_0 = 0b101010101010101010;

  vector<ll> C(N);
  vector<ll> P(N);

  ll n_operation;
  
  for(ll color=0; !(color>>N); ++color) {
    ll sum_color = 0;
    ll pos_1 = color ^ pos_0;
    for(ll i=0; i<N; ++i) {
      C[i] = ((color>>i)&1 ? B[i] : A[i]);
      P[i] = (pos_1>>i)&1;
      sum_color += ((color>>i)&1);
    }
    if (sum_color&1) continue;

    vector<ll> C_sorted(C);
    sort(C_sorted.begin(), C_sorted.end());
    
    n_operation = 0;
    bool found;
    for(ll i=0; i<N; ++i) {
      found = false;
      ll j=i;
      for(; j<N; ++j) {
        if(C[j]==C_sorted[i] && P[j]==(i&1)) { found = true; break; }
      }

      if (found) {
        n_operation += j-i;
        for(ll k=j; k>i; --k) {
          ll bC = C[k]; C[k]=C[k-1]; C[k-1]=bC;
          ll bP = P[k]; P[k]=P[k-1]; P[k-1]=bP;
        }
        
      } else { break; }

    }

    if(found) ans = min(ans, n_operation);
    
  }

  cout << (ans<1e10 ? ans : -1) << endl;
  return 0;
}
