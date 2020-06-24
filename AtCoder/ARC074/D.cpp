#include<vector>
#include<set>
#include<iostream>
#include<algorithm>
using namespace std;
#define ll long long

template<class T>
void print(T& arr){
  for (auto itr = arr.begin(); itr!=arr.end(); ++itr) cout << (*itr) << " "; cout << endl;  
}

int main(){
  ll N, a;
  cin >> N;
  vector<ll> A;
  for(int i=0; i<3*N; ++i) {
    cin >> a;
    A.emplace_back(a);
  }

  multiset<ll> min(A.begin(), A.begin()+N), max(A.end()-N, A.end());

  //min.sort();
  //max.sort();

  vector<ll> S_l{0}, S_r{0};
  for(int i=0; i<N; ++i){
    S_l[0]+=A[i];
    S_r[0]+=A[2*N+i];
  }

  ll s_l, s_r;
  auto ptr_min = min.begin();
  auto ptr_max = --max.end();
  for(int i=0; i<N; ++i) {
    a = A[N+i];
    if (a <= *ptr_min){
      s_l = a;
    }else{
      s_l = *ptr_min;
      //auto ptr_insert = min.lower_bound(a);
      min.insert(a);
      ++ptr_min;
    }
    S_l.emplace_back(S_l[i] + a - s_l);

    a = A[2*N-i-1];
    if (a >= *ptr_max){
      s_r = a;
    }else{
      s_r = *ptr_max;
      //auto ptr_insert = max.upper_bound(a);
      max.insert(a);
      --ptr_max;
    }
    S_r.emplace_back(S_r[i] + a - s_r);
  }

  ll ans = S_l[0]-S_r[N];
  for(int i=1; i<N+1; ++i) {
    if(S_l[i]-S_r[N-i] > ans) ans = S_l[i]-S_r[N-i];
  }

  cout << ans << endl;
  
  return 0;
}
