#include<iostream>
#include<set>
using namespace std;

struct Data {
  //public:
  int x, y, z;
  Data(int _x, int _y, int _z): x(_x), y(_y), z(_z) {}
};

struct Cmp_x {
  bool operator()(Data l, Data r) const { return l.x<r.x; }
};

int main(){
  Data d1(1,2,2), d2(1,5,5), d3(2,5,5);
  multiset<Data, Cmp_x> s;

  s.insert(d2);
  s.insert(d3);
  s.insert(d1);
  for(auto itr=s.begin(); itr!=s.end(); ++itr) { cout << (itr->x) << "," << (itr->y) << "," << (itr->z) << " "; } cout << endl;

  return 0;
}
