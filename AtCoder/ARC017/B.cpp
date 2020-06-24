#include<iostream>
using namespace std;
#define ll long long

int main(){
  ll N, K, A, P=99999999, T, ans=0;
  cin >> N >> K;

  for(ll i=0; i<N; ++i){
    cin >> A;
    if(A<=P) T=i;
    if(i-T+1>=K) ++ans;
    P=A;
  }

  cout << ans << endl;
  
  return 0;
}
