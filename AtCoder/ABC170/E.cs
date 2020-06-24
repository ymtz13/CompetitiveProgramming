using System;
using System.Collections.Generic;
using System.Linq;

delegate T Function<T>(T v1, T v2);

class Yochien
{
    int Count = 0;
    int cellsize = 500;
    List<int> data;
    List<int> cells;

    public Yochien() {
        data = new List<int>();
        cells = new List<int>();
    }
    
    public int Add(int v) {
        var idata = data.Count;
        var icell = idata/cellsize;
        data.Add(v);
        if(icell==cells.Count) cells.Add(0);
        cells[icell] = Math.Max(cells[icell], v);

        ++Count;

        return idata;
    }

    public int Update(int idata, int v) {
        //Console.WriteLine($"Update {idata} {v}");
        //Console.WriteLine($"  data: " + string.Join(" ", data));
        
        var icell = idata/cellsize;
        var value_old = data[idata];
        data[idata] = v;
        var max_new = 0;
        for(int i=icell*cellsize; i<(icell+1)*cellsize && i<data.Count; ++i) {
            max_new = Math.Max(max_new, data[i]);
        }
        cells[icell] = max_new;

        if(v==0) --Count;

        return value_old;
    }

    public int Max() {
        if(Count==0) return 2000000000;
        var max = 0;
        for(int i=0; i<cells.Count; ++i) {
            max = Math.Max(max, cells[i]);
        }
        return max;
    }
}

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

class Program
{
    static void Main()
    {
        //->  //var st = new SegTree<int>(14, Math.Max);
        //->  var st = new SegTree<int>(14, delegate(int x, int y) {return x+y;});
        //->  st.Print();
        //->  
        //->  st.Update(5, 3);
        //->  st.Print();
        //->  st.Update(8, 4);
        //->  st.Print();
        //->  st.Update(10, 2);
        //->  st.Print();
        //->  
        //->  Console.WriteLine(st.Query(3, 7));
        
        var NQ = Console.ReadLine().Split().Select(int.Parse).ToList();
        int N = NQ[0], Q = NQ[1];
        int M = 200000;

        var st = new SegTree<int>(M, Math.Min);

        var Y = new Yochien[M];
        for(int i=0; i<M; ++i) Y[i] = new Yochien();

        var LY = new int[N]; // i-th infant belongs to LY[i]-th Yochien.
        var LI = new int[N]; // i-th infant belongs to LI-th index (of LY[i]-th Yochien).
        
        for(int i=0; i<N; ++i) {
            var AB = Console.ReadLine().Split().Select(int.Parse).ToList();
            int A = AB[0], B = AB[1];
            
            LY[i] = B-1;
            LI[i] = Y[LY[i]].Add(A);

            //Console.WriteLine($"{LY[i]}, {LI[i]}");
        }

        for(int i=0; i<M; ++i) st.Update(i, Y[i].Max());
        
        for(int iq=0; iq<Q; ++iq) {
            var CD = Console.ReadLine().Split().Select(int.Parse).ToList();
            int C = CD[0], D = CD[1];

            var ly_old = LY[C-1];
            var y_old = Y[ly_old];
            int A = y_old.Update(LI[C-1], 0);
            
            var ly_new = LY[C-1] = D-1;
            var y_new = Y[ly_new];
            LI[C-1] = y_new.Add(A);

            st.Update(ly_old, y_old.Max());
            st.Update(ly_new, y_new.Max());
            Console.WriteLine(st.Query(0, st.Count));
        }
        
        
    }
}
