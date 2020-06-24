#include<iostream>
#include<algorithm>
using namespace std;

int main(){
  int X, Y, Z, K;
  cin >> X >> Y >> Z >> K;
  int L = min(X*Y, K);

  long long A[X], B[Y], C[Z], AB[X*Y], ABC[L*Z];
  for(int i=0; i<X; ++i) cin >> A[i];
  for(int i=0; i<Y; ++i) cin >> B[i];
  for(int i=0; i<Z; ++i) cin >> C[i];

  for(int i=0; i<X; ++i)
  for(int j=0; j<Y; ++j)
    AB[i*Y+j] = A[i] + B[j];

  sort(AB, AB+X*Y, [](const long long& x, const long long& y){ return x>y; });

  for(int i=0; i<L; ++i)
  for(int j=0; j<Z; ++j)
    ABC[i*Z+j] = AB[i] + C[j];

  sort(ABC, ABC+L*Z, [](const long long& x, const long long& y){ return x>y; });
  
  for(int i=0; i<K; ++i) cout << ABC[i] << endl;

  return 0;
}
