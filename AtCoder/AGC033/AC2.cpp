#include<iostream>
#include<vector>
using namespace std;


int main()
{
  int H,W;
  cin >> H >> W;

  vector<int> black;
  vector<int> black_new;
  vector<int> cell;

  string s;

  int n_black=0;
  
  for(int irow=0; irow<H; ++irow){
    cin >> s;
    for(int icol=0; icol<W; ++icol){      
      if (s[icol]=='#'){
        black.push_back(icol);
        black.push_back(irow);
        cell.push_back(1);
        n_black+=1;
      }else{
        cell.push_back(0);
      }
    }
  }

  int n_operation=0;
  while(n_black!=H*W){
    n_operation++;
    
    for(int ib=0; ib<black.size()/2; ++ib){
      int bx = black[ib*2];
      int by = black[ib*2+1];

      if(bx-1>=0 && cell[W*by+bx-1]==0){ 
        black_new.push_back(bx-1);
        black_new.push_back(by);
        cell[W*by+bx-1]=1;
        n_black+=1;
      }
      if(bx+1<W && cell[W*by+bx+1]==0){ 
        black_new.push_back(bx+1);
        black_new.push_back(by);
        cell[W*by+bx+1]=1;
        n_black+=1;
      }
      if(by-1>=0 && cell[W*(by-1)+bx]==0){ 
        black_new.push_back(bx);
        black_new.push_back(by-1);
        cell[W*(by-1)+bx]=1;
        n_black+=1;
      }
      if(by+1<H && cell[W*(by+1)+bx]==0){ 
        black_new.push_back(bx);
        black_new.push_back(by+1);
        cell[W*(by+1)+bx]=1;
        n_black+=1;
      }
    }

    black.clear();
    for(int i=0; i<black_new.size(); ++i)
      black.push_back(black_new[i]);
    black_new.clear();
    
    cout << endl;
    for(int irow=0; irow<H; ++irow){
      for(int icol=0; icol<W; ++icol){
        cout << cell[irow*W+icol];
      }
      cout<<endl;
    }
    
  }
    

  cout << n_operation << endl;
  
  return 0;
}
