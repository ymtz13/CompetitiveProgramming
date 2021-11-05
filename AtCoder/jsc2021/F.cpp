#include<iostream>
#include<set>
#include<vector>
using namespace std;
#define ll long long

int main(){
  ll N, M, Q;
  cin >> N >> M >> Q;

  vector<ll> A(N), B(M), AP(N), BP(M);
  multiset<ll> AM(A.begin(), A.end()), BM(B.begin(), B.end());
  cout << A[N-1] << B[N-1] << endl;

  ll ans = 0;
  for(int i=0; i<Q; ++i) {
    ll T, X, Y;
    cin >> T >> X >> Y;

    if(T==1){
      ll aold = A[X-1];
      AM.erase(aold);
      ans -= 

      A[X-1] = Y;


    }else {


    }

    cout << T << X << Y;
  }
}