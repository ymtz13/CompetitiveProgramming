#include<iostream>
using namespace std;
#define ll long long

int main(){
  ll H, W, A, B;
  cin >> H >> W >> A >> B;

  for(ll h=0; h<H; ++h){
    for(ll w=0; w<W; ++w){
      ll c = ((h>=B || w>=A) && !(h>=B && w>=A)) ? 1 : 0;
      cout << c;
    }
    cout << endl;
  }

  return 0;
}


/*


3 3 1 1

11100
11100
00011
00011

100
011
011

 */
