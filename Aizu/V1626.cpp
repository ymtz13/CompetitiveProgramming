#include<iostream>
#include<cmath>
using namespace std;

int main(){
  while(true){
    int b;
    cin >> b;
    if(b==0) break;

    int s = b*2;
    int w = sqrt(s);
    if(w*w==s) --w;

    for(; w>=1; w--) {
      if(s%w==0 && w%2!=(s/w)%2) break;
    }

    int h = s/w;
    int x = (h-w+1)/2;
    
    cout << x << " " << w << endl;
  }

  return 0;
}
