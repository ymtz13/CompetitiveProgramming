#include<iostream>
using namespace std;
#define ll long long

int main() {
  ll N, x;
  cin >> N >> x;

  ll a[N];
  for(ll i=0; i<N; ++i) cin >> a[i];

  ll dp[N][N], sum[N];
  for(ll j=0; j<N; ++j) sum[j]=0;

  for(ll i=0; i<N; ++i) dp[i][0] = a[i];
                          
  for(ll j=1; j<N; ++j) {
    for(ll i=0; i<N; ++i){
      if (dp[i][j-1]<dp[(i-1+N)%N][j-1]) {
        dp[i][j] = dp[i][j-1];
      }else{
        dp[i][j] = dp[(i-1+N)%N][j-1];
      }
    }    
  }
  
  for(ll i=0; i<N; ++i) for(ll j=0; j<N; ++j) sum[j]+=dp[i][j];

  ll min=sum[0];
  for(ll j=1; j<N; ++j) { if(min>sum[j]+x*j) min=sum[j]+x*j; }

  cout << min << endl;
  
  return 0;
}
