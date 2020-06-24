#include<iostream>
using namespace std;

int main(){
  int H, W;
  cin >> H >> W;
  
  string S[H];
  for(int i=0; i<H; ++i){ cin >> S[i]; }

  int d[H][W];

  for(int h=0; h<H; ++h) {
    int m=-1;
    for(int w=0; w<W; ++w) {
      if (S[h][w]=='.'){ d[h][w] = w-m; }
      else{ d[h][w] = 0; m=w; }
    }
  }

  for(int h=0; h<H; ++h) {
    int m=W;
    for(int w=W-1; w>=0; --w) {
      if (S[h][w]=='.'){ d[h][w] += m-w; }
      else{ m=w; }
    }
  }

  for(int w=0; w<W; ++w) {
    int m=-1;
    for(int h=0; h<H; ++h) {
      if (S[h][w]=='.'){ d[h][w] += h-m; }
      else{ m=h; }
    }
  }

  for(int w=0; w<W; ++w) {
    int m=H;
    for(int h=H-1; h>=0; --h) {
      if (S[h][w]=='.'){ d[h][w] += m-h; }
      else{ m=h; }
    }
  }
  

  int max_l=0;
  for(int h=0; h<H; ++h)
  for(int w=0; w<W; ++w)
    max_l = max(max_l, d[h][w]-3);

  cout << max_l << endl;

  return 0;
}
