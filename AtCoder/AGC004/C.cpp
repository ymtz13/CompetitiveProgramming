#include<iostream>
using namespace std;
#define ll long long

int main(){
  ll H, W;
  cin >> H >> W;

  bool A[H][W];
  string s;
  for(ll h=0; h<H; ++h){
    cin >> s;
    for(ll w=0; w<W; ++w){
      A[h][w] = s[w]=='#';
    }
  }

  for(ll h=0; h<H; ++h){
    for(ll w=0; w<W; ++w) cout << ((w==0 || (h%2==0 && w<W-1) || A[h][w]) ? '#' : '.');
    cout << endl;
  }
  
  cout << endl;

  for(ll h=0; h<H; ++h){
    for(ll w=0; w<W; ++w) cout << ((w==W-1 || (h%2==1 && w>0) || A[h][w]) ? '#' : '.');
    cout << endl;
  }
  
  return 0;
}
