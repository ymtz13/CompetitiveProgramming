#include<iostream>
#include<vector>

int main(){
  std::string s;
  std::cin >> s;
  long long mod = 1000000007;

  int T[6][10];
  int r=1;
  for(int i=0; i<6; ++i){
    for(int j=0; j<10; ++j){
      T[i][j] = (j*r)%13;
    }
    r*=10;
  }

  long long _dp1[13], _dp2[13];
  long long *dp = _dp1, *dp_new = _dp2, *dp_swap;
  dp[0]=1;
  for(int i=1; i<13; ++i) dp[i]=0;

  int k = s.size()-1;
  for(int i=0; i<s.size(); ++i, --k){
    for(int j=0; j<13; ++j) dp_new[j]=0;

    if(s[i]=='?'){
      for(int r=0; r<10; ++r){
        int m = T[k%6][r];
        for(int n=0; n<13; ++n) dp_new[(n+m)%13] += dp[n];
      }
    }else{
      int m = T[k%6][(int)(s[i]-'0')];
      for(int n=0; n<13; ++n) dp_new[(n+m)%13] = dp[n];
    }
    
    dp_swap = dp_new; dp_new = dp; dp = dp_swap;
    for(int j=0; j<13; ++j) dp[j]%=mod;
  }

  std::cout << dp[5] << std::endl;
  return 0;
}
