#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main(){
  int N, M;
  cin >> N;
  cin >> M;
  vector<int> A(N);
  for(int i=0; i<N; ++i){
    cin >> A[i];
  }
  
  for(int i=0; i<M; ++i){
    int B, C;
    cin >> B;
    cin >> C;

    sort(A.begin(), A.end());
    
    int j=B-1;
    for(; j>=0; --j){
      if(A[j]<C) break;
    }
    for(; j>=0; --j) A[j] = C;
    
  }

  return 0;
}


111222 33 
331222 44
