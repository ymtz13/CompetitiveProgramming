using System;

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


class Program
{
    static void Main()
    {
        //var st = new SegTree<int>(14, Math.Max);
        var st = new SegTree<int>(14, delegate(int x, int y) {return x+y;});
        st.Print();

        st.Update(5, 3);
        st.Print();
        st.Update(8, 4);
        st.Print();
        st.Update(10, 2);
        st.Print();

        Console.WriteLine(st.Query(3, 7));

        
    }
}
