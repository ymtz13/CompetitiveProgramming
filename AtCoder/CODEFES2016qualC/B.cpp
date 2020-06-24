#include<iostream>
#include<set>
using namespace std;
#define ll long long

struct Cake{
  ll id, n;
  Cake(ll _id, ll _n):id(_id), n(_n) {}
};

bool operator <(const Cake& lhs, const Cake& rhs) { return lhs.n>rhs.n; }

template<class T>
void print(T& cakes) {
  for(auto itr=cakes.begin(); itr!=cakes.end(); ++itr) {
    cout << itr->id << ":" << itr->n << "  ";
  }
  cout << endl;
}
  

int main(){
  ll K, T, a;
  cin >> K >> T;

  multiset<Cake> cakes;
  for(ll i=0; i<T; ++i) {
    cin >> a;
    cakes.emplace(i,a);
  }

  ll id_prev = -1;
  for(ll i=0; i<K; ++i) {
    auto itr = cakes.begin();
    if (itr->id == id_prev) ++itr;

    id_prev = itr->id;
    ll n = itr->n-1;
    cakes.erase(itr);
    
    if (n>0) cakes.emplace(id_prev, n);

    if (cakes.size()==1) break;
  }

  ll streak = cakes.begin()->n-1;
  if (id_prev == cakes.begin()->id) ++streak;
  cout << streak << endl;

  return 0;
}
