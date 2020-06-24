#include<iostream>
#include<vector>
#include <algorithm>
using namespace std;

void func(int t, vector<long long>& f, vector<long long>& n, vector<int>& v, vector<long long>& y){
  if(t == f.size()){
    long long yy=1;
    for(int k=0; k< f.size(); ++k) for(int l=0; l<v[k]; ++l) yy*=f[k];
    y.push_back(yy);
    return;
  }
  for(int j=0; j<n[t]+1; ++j){
    v[t]=j;
    func(t+1, f, n, v, y);
  }
  return;
}
  

int main(){
  long long N, K, S=0;
  cin >> N >> K;

  long long A[N];
  for(long long i=0; i<N; ++i){
    cin >> A[i];
    S += A[i];
  }

  int n_factor = 0;
  vector<long long> f;
  vector<long long> n;
  long long s = S;
  for(long long i=2; i*i<=s; ++i){
    if(s%i>0) continue;

    ++n_factor;
    f.push_back(i);
    n.push_back(0);
    while(s%i==0){
      n[n_factor-1]++;
      s/=i;
    }
  }

  if(s>1){
    ++n_factor;
    f.push_back(s);
    n.push_back(1);
  }

  vector<int> v;
  for(int i=0; i<n.size(); ++i) v.push_back(0);
  vector<long long> y;
  func(0, f, n, v, y);

  long long m = 0;
  
  for(int iy=0; iy<y.size(); ++iy){
    long long yy = y[iy];

    vector<long long> cost;
    for(int i=0; i<N; ++i){
      cost.push_back(A[i]%yy);
    }
    sort(cost.begin(), cost.end());

    int tgt_down=0, tgt_up=N-1, total_cost=0;
    while(tgt_down<tgt_up){
      if(cost[tgt_down]<yy-cost[tgt_up]){
        total_cost += cost[tgt_down];
        cost[tgt_up] += cost[tgt_down];
        cost[tgt_down] = 0;        
      }else{
        total_cost += yy-cost[tgt_up];
        cost[tgt_down]-=yy-cost[tgt_up];
        cost[tgt_up]=yy;
      }
      if(cost[tgt_up]==yy) tgt_up--;
      if(cost[tgt_down]==0) tgt_down++;
    }

    //cout <<"yy "<< yy << " tc " << total_cost << endl;
    if(total_cost <= K){ m = max(m,yy);}
  }

  cout << m << endl;;
  
  return 0;
}
