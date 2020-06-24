#include<iostream>
#include<sstream>
#include<vector>
using namespace std;

struct UnionFind {
  vector<int> par;
  
  UnionFind(int n) : par(n, -1) {}

  void merge(int x, int y){
    x = find(x);
    y = find(y);

    if(x==y) return;

    if(par[y]<par[x]){
      int buf = x; x = y; y = buf;
    }

    par[x] += par[y];
    par[y] = x;
  }
  
  int find(int x){
    if (par[x]<0) return x;
    return par[x]=find(par[x]);
  }

  void print(){
    for(int i=0; i<par.size(); ++i) { printf("%3d ", i); }
    cout << endl;
    for(int i=0; i<par.size(); ++i) { printf("%3d ", par[i]); find(i); }
    cout << endl;
    for(int i=0; i<par.size(); ++i) { printf("%3d ", par[i]); }
    cout << endl;
  }

  void test(){
    while(true){
      int x,y;
      cin >> x >> y;
      merge(x,y);
      print();
    }
  }
};

struct Edge {
  int a,b,d;
  
  Edge() : a(0), b(0), d(0){}
  Edge(int _a, int _b, int _d) : a(_a), b(_b), d(_d){}
};

bool operator<(const Edge& e1, const Edge& e2){ return e1.d < e2.d; }

int main(){
  while(true){
    int n,m;
    cin >> n;
    if(n==0) break;
    cin >> m;
    vector<Edge> edges;

    UnionFind uf(n);
    
    for(int i=0; i<m; ++i){
      string s, buf;
      cin >> s;
      stringstream ss(s);
      Edge e;
      getline(ss, buf, ',');
      e.a = stoi(buf);
      getline(ss, buf, ',');
      e.b = stoi(buf);
      getline(ss, buf, ',');
      e.d = stoi(buf);

      edges.push_back(e);
    }

    sort(edges.begin(), edges.end());

    int n_lantern = 0;
    for(vector<Edge>::const_iterator itr = edges.begin(); itr != edges.end(); ++itr){
      if(uf.find(itr->a)!=uf.find(itr->b)){
        uf.merge(itr->a, itr->b);
        n_lantern += itr->d/100-1;
      }
    }

    cout << n_lantern << endl;
  }

  return 0;
}
