#include<iostream>
using namespace std;

int main(){
  int N;
  long long K;
  cin >> N >> K;

  long long a[N], s[N+1];
  s[0] = 0;
  for(int i=0; i<N; ++i){
    cin >> a[i];
    s[i+1] = s[i] + a[i];
  }

  int j=0;
  long long n=0;
  for(int i=0; i<N; ++i)
  for(; j<N+1 && s[i+1]-s[j]>=K; j++) n += N-i;

  cout << n << endl;

  return 0;
}
