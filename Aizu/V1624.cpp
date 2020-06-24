#include<iostream>
using namespace std;

int main(){
  while(true){
    int n;
    cin >> n;
    if(n==0) break;

    int a[n];
    int s=0, b;
    for(int i=0; i<n; ++i){
      cin >> b;
      s+=b;
      a[i]=b*n;
    }

    b=0;
    for(int i=0; i<n; ++i){
      if(a[i]<=s)++b;
    }
    cout<<b<<endl;
  }

  return 0;
}
