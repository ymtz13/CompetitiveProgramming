using System;
using System.Collections.Generic;
using System.Linq;

delegate T Function<T>(T v1, T v2);

class SegTree<T>
{

    public int Count { get; }
    
    int n_layer;
    int[] segsize;
    T[][] data;

    Function<T> function;
    
    public SegTree(int N, Function<T> function, T fill=default(T))
    {
        Count=N;

        this.function=function;
        
        n_layer=1;
        for(int k=1; k<N; k<<=1) n_layer+=1;

        segsize = new int[n_layer];
        data = new T[n_layer][];
        for(int l=0; l<n_layer; ++l) {
            segsize[l] = 1<<(n_layer-1-l);
            data[l] = new T[1<<l];
            for(int j=0; j<(1<<l); ++j) data[l][j]=fill;
        }
    }
    
    public void Update(int index, T value) {
        data[n_layer-1][index] = value;
        for(int l=n_layer-2; l>=0; --l) {
            index = index/2;
            data[l][index] = function(data[l+1][index*2], data[l+1][index*2+1]);
        }
    }

    public T Query(int ibgn, int iend, int l=0) {
        int ssize = segsize[l];
        if(ibgn%ssize==0 && iend-ibgn==ssize) return data[l][ibgn/ssize];

        int imid = ibgn - ibgn%ssize + ssize/2;
        if(iend<=imid || imid<=ibgn) return Query(ibgn, iend, l+1);
        return function(Query(ibgn, imid, l+1), Query(imid, iend, l+1));
    }
    

    public void Print()
    {
        Console.WriteLine($"Count   : {Count}");
        Console.WriteLine($"n_layer : {n_layer}");
        for(int l=0; l<n_layer; ++l) {
            Console.WriteLine($"[{l}] "+string.Join(" ", data[l]));
        }
    }
}

class XYPoint
{
  public int X, Y;
  public XYPoint(int x, int y) {
    X = x; Y = y;
  }
}

class Program
{
  static void Main()
  {
    var HWN = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
    int H = HWN[0], W = HWN[1], N = HWN[2];

    var Ymin = new int[W];
    for(int w=0; w<W; ++w) Ymin[w] = H;

    var Xmin = new int[H];
    for(int h=0; h<H; ++h) Xmin[h] = W;

    var XYList = new List<XYPoint>();

    for(int i=0; i<N; ++i) {
      var YX = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
      int Y = YX[0]-1, X = YX[1]-1;

      XYList.Add(new XYPoint(X, Y));

      Ymin[X] = Math.Min(Ymin[X], Y);
      Xmin[Y] = Math.Min(Xmin[Y], X);
    }

    XYList.Sort(delegate(XYPoint p1, XYPoint p2) { return p1.Y - p2.Y; } );

    int xEnd = Xmin[0];
    int yEnd = Ymin[0];

    long ans = 0;

    for(int x=0; x<xEnd; ++x) ans += Ymin[x];

    var st = new SegTree<int>(W+2, delegate(int x, int y) { return x + y; });

    for(int x = xEnd; x<W; ++x) st.Update(x, 1);

    int n = 0;
    for(int y=0; y<yEnd; ++y){
      
      while(n<N && XYList[n].Y<=y) {
        var p = XYList[n];
        st.Update(p.X, 1);
        n += 1;
      }

      int add = st.Query(0, Xmin[y]);
      ans += add;
    }

    Console.WriteLine(ans);
  }
}