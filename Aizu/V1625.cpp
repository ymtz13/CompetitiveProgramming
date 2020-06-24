#include<iostream>
using namespace std;
#define L_MAX 64

int main(){
  while(true){
    int n, m, t, p;
    cin >> n >> m >> t >> p;
    if(n==0) break;

    int ovlp[3][L_MAX];
    int* ovlp_h = ovlp[0];
    int* ovlp_v = ovlp[1];
    int* ovlp_buf = ovlp[2];
    
    for(int i=0; i<L_MAX; ++i){
      if(i<n) { ovlp_h[i]=1; } else { ovlp_h[i]=0; }
      if(i<m) { ovlp_v[i]=1; } else { ovlp_v[i]=0; }
    }

    for(int i=0; i<t; ++i){
      int d,c;
      cin >> d >> c;
      
      int** ovlp_tgt;
      if(d==1){
        ovlp_tgt = &ovlp_h;
        n -= min(c, n-c);
      }
      else {
        ovlp_tgt = &ovlp_v;
        m -= min(c, m-c);
      }
      
      for(int j=0; j<L_MAX; ++j){
        if(c+j<L_MAX){ ovlp_buf[j] = (*ovlp_tgt)[c+j]; } else { ovlp_buf[j]=0; }
        if(j<c) { ovlp_buf[j] += (*ovlp_tgt)[c-j-1]; }
      }

      int* buf = ovlp_buf;
      ovlp_buf = (*ovlp_tgt);
      (*ovlp_tgt) = buf;
    }

    int x, y;
    for(int i=0; i<p; ++i){
      cin >> x >> y;
      cout << ovlp_h[x]*ovlp_v[y] <<endl;
    }
    
  }

  return 0;
}
