#include<iostream>
using namespace std;
#define ll long long

int main(){
  ll X;
  cin >> X;

  ll x=0, i;
  for(i=1; i<X; ++i){
    x+=i;
    if(x>=X) break;
  }

  cout << i <<endl;  
  
  return 0;
}
