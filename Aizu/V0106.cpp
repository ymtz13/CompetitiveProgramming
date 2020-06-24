#include<iostream>
using namespace std;

#define INF 10000000

int main(){
  int dp[51];
  dp[0] = 0;
  dp[1] = INF;
  for(int w=2; w<=50; ++w){
    dp[w] = dp[w-2]+380;
    if(w- 3>=0) { dp[w] = min(dp[w], dp[w- 3]+ 550); }
    if(w- 5>=0) { dp[w] = min(dp[w], dp[w- 5]+ 850); }
    if(w-10>=0) { dp[w] = min(dp[w], dp[w-10]+1520); }
    if(w-12>=0) { dp[w] = min(dp[w], dp[w-12]+1870); }
    if(w-15>=0) { dp[w] = min(dp[w], dp[w-15]+2244); }    
  }

  int p;
  while(true){
    cin >> p;
    if(p==0){ break; }
    cout << dp[p/100] << endl;
  }

  return 0;
}
