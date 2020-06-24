using System;
using System.Collections.Generic;

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

class Point{ public int w,h; }

class Program
{
    static void Main()
    {
        var N = int.Parse(Console.ReadLine());
        var L = new List<Point>();
        for(int i=0; i<N; ++i) {
            var buf = Console.ReadLine().Split(new char[]{' '});
            var p = new Point();
            p.w = int.Parse(buf[0]);
            p.h = int.Parse(buf[1]);
            L.Add(p);
        }

        L.Sort(delegate(Point p1, Point p2){
                if(p1.h!=p2.h) return p1.h-p2.h;
                return -(p1.w-p2.w);
            });

        var st = new SegTree<int>(100001, Math.Max);
        foreach(var p in L) {
            st.Update(p.w, st.Query(0, p.w)+1);
        }

        Console.WriteLine(st.Query(0, st.Count));
        
    }
}
