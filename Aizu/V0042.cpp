#include<iostream>
#include<sstream>
using namespace std;


int main(){
  for(int idata=1; ; ++idata){
    int W, N;
    cin >> W;
    if(W==0) break;
    cin >> N;

    int dp[N+1][W+1];
    for(int iw=0; iw<=W; ++iw) dp[0][iw]=0;
  
    for(int in=1; in<=N; ++in){
      string s, buf;
      cin >> s;
      stringstream ss(s);
      getline(ss, buf, ',');
      int v = stoi(buf);
      getline(ss, buf, ',');
      int w = stoi(buf);

      for(int iw=0; iw<=W; ++iw){
        int jw = iw-w;
        if(jw<0){ dp[in][iw] = dp[in-1][iw]; continue;}
        dp[in][iw] = max(dp[in-1][iw], dp[in-1][jw]+v);
      }
    }

    int v_max = dp[N][W];
    int w_max;
    for(int iw=W-1; iw>=0; --iw){
      if(dp[N][iw] < v_max){ w_max = iw+1; break; }
    }

    cout << "Case " << idata << ":"<<endl;
    cout << v_max << endl;
    cout << w_max << endl;
  }

  return 0;
}
