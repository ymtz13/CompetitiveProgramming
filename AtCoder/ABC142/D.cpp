#include<iostream>
using namespace std;
#define ll long long

int main(){
  ll A, B;
  cin >> A >> B;
  while(B>0){
    ll C = A%B; A=B; B=C;
  }

  ll p=2, ans=1;
  while(p*p<=A){
    ll c=0;
    while(A%p==0){
      A/=p;
      c=1;
    }
    if (c>0) ++ans;
    ++p;
  }
  if (A>1) ++ans;

  cout << ans << endl;

  return 0;
}
