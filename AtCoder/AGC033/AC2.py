#include<iostream>
#include<vector>
using namespace std;


int main()
{
  int H,W;
  cin >> H >> W;

  vector<int> black;
  vector<int> white;

  string s;
  
  for(int irow=0; irow<H; ++irow){
    cin >> s;
    for(int icol=0; icol<W; ++icol){
      if (s[icol]=='#'){
        black.push_back(irow);
        black.push_back(icol);
      }else{
        white.push_back(irow);
        white.push_back(icol) ;       
      }
    }
  }

  int dmax=0;
  for(int iw=0; iw<white.size()/2; ++iw){
    int dmin=10000000;
    for(int ib=0; ib<black.size()/2; ++ib){
      dmin = min(dmin, abs(black[ib*2]-white[iw*2]) + abs(black[ib*2+1]-white[iw*2+1]));
      if(dmin<dmax){ break; }
    }
    dmax = max(dmax, dmin);
  }

  cout << dmax << endl;
  
  return 0;
}
