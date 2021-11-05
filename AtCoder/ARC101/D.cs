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

class Program {

  static int N;
  static List<int> A;
  static int offset = 100005;

  static bool check(int X) {
    var st = new SegTree<int>(200010, delegate(int x, int y) { return x + y; });
    st.Update(offset, 1);
    int S = 0, R = 0;
    for(int i=0; i<N; ++i) {
      S += (A[i] <= X ? +1 : -1);
      R += st.Query(0, S + offset);
      //Console.WriteLine($"{i}, {A[i]}, {S}, {R}");
      st.Update(S + offset, st.Query(S + offset, S + offset + 1) + 1);
    }
    return R > (N*(N+1)/2)/2;
  }

  static void Main() {
    N = int.Parse(Console.ReadLine());
    A = Console.ReadLine().Split(' ').Select(int.Parse).ToList();

    int ok = 1000000000, ng = 0;
    while(ok-ng>1) {
      int tgt = (ok+ng)/2;
      if(check(tgt)) {
        ok = tgt;
      } else {
        ng = tgt;
      }
    }

    Console.WriteLine(ok);
  }
}