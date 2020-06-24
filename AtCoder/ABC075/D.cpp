#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
#define ll long long

struct Point {
  ll x, y;

  Point(ll x, ll y) { this->x = x; this->y = y; }
};

struct _cmp_x {
  bool operator() (const Point& a, const Point& b) const { return a.x<b.x; }
} cmp_x;

struct _cmp_y{
  bool operator() (const Point& a, const Point& b) const { return a.y<b.y; }
} cmp_y;


int main(){
  ll N, K, x, y;
  cin >> N >> K;

  vector<Point> P;
  for(int i=0; i<N; ++i) {
    cin >> x >> y;
    P.emplace_back(x,y);
  }
  
  sort(P.begin(), P.end(), cmp_x);
  //sort(P.begin(), P.end(), [](const Point& a, const Point& b) { return a.y<b.y; } );

  ll ans=LLONG_MAX;
  ll R = N-K;
  for(ll remove_l=0; remove_l<=R;          ++remove_l)
  for(ll remove_r=0; remove_l+remove_r<=R; ++remove_r){
    vector<Point> P2(P.begin()+remove_l, P.end()-remove_r);
    sort(P2.begin(), P2.end(), cmp_y);
    //for(auto itr = P2.begin(); itr!=P2.end(); ++itr) cout << "(" << itr->x << "," << itr->y << ") ";
    //cout << endl;
    
    for(ll remove_u=0; remove_l+remove_r+remove_u<=R; ++remove_u){
      const auto itr_bgn = P2.begin()+remove_u;//, itr_end = P2.begin()+remove_u+K;
      const auto itr_end = itr_bgn + K;
      
      ll h = (itr_end-1)->y - itr_bgn->y;
      ll x_max, x_min;
      x_max = x_min = itr_bgn->x;
      for(auto itr = itr_bgn; itr!=itr_end; ++itr) {
        if(itr->x > x_max) x_max=itr->x;
        if(itr->x < x_min) x_min=itr->x; 
      }
      ll s = (x_max-x_min)*h;

      if(ans>s) ans=s;

      //cout << remove_l << "," << remove_r << "," << remove_u << "," << h << "," << s << " ";
      //for(auto itr = itr_bgn; itr!=itr_end; ++itr) cout << "(" << itr->x << "," << itr->y << ") ";
      //cout << endl;
    }
      
  }
  

  cout << ans << endl;
  
  return 0;
}
