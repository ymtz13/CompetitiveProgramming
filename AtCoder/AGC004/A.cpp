#include<iostream>
using namespace std;
#define ll long long

int main(){
  ll A, B, C;
  cin >> A >> B >> C;
  if ((A*B*C)%2==0) { cout << 0 << endl; return 0; }

  cout << min(min(A*B, B*C), C*A) << endl;
  
  return 0;
}
