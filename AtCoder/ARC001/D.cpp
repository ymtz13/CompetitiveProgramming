#include<iostream>
#include<vector>
#include<cmath>
using namespace std;
#define ll long long

template<class T>
void print(T& arr) {
  for(auto itr=arr.begin(); itr!=arr.end(); ++itr) cout << (*itr) << " "; cout << endl;
}

double dist(ll x1, ll y1, ll x2, ll y2) {
  ll dx = x1-x2, dy = y1-y2;
  return sqrt(dx*dx+dy*dy);
}

int main(){
  ll N, start, goal;
  cin >> N;
  cin >> start >> goal;

  vector<ll> L(N+1), R(N+1);
  for(int i=0; i<N+1; ++i) {
    cin >> L[i] >> R[i];
  }

  ll x0 = start, y0 = 0;
  double ans = 0;

  for(int y=1; y<N+1; ++y) {
    double x = x0+(double)(goal-x0)*(y-y0)/(N-y0);
    if x<

  }
  
  return 0;
}
