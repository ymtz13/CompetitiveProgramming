#include<iostream>
#include<vector>
using namespace std;
#define N  40
#define M 100
#define B 300

int main(){
  int tmp;
  cin >> tmp >> tmp >> tmp;

  int gy, gx;
  cin >> gy >> gx;

  vector<int> ry(M), rx(M), c(M), by(B), bx(B);
  for(int m=0; m<M; ++m){
    string _c;
    cin >> ry[m] >> rx[m] >> _c;
    if(_c=="U") c[m]=1;
    if(_c=="D") c[m]=2;
    if(_c=="L") c[m]=3;
    if(_c=="R") c[m]=4;
  }

  for(int b=0; b<B; ++b) cin >> by[b] >> bx[b];


  
  cout << (N-1)*2 << endl;
  for(int i=1; i<N; ++i) cout << gy << " " << (gx+i)%N << " L" << endl;
  for(int i=1; i<N; ++i) cout << (gy+i)%N << " " << gx << " U" << endl;


  return 0;
}
