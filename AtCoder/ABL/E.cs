using System;

delegate T MergeFunction<T>(T v1, T v2, STParams p);
delegate T ResolveFunction<T, U>(T value, U lazyValue, STParams p);

class STParams {
    public int layer;
    public int segsize;
    public int index;

    public STParams(int layer, int segsize, int index) {
        this.layer = layer;
        this.segsize = segsize;
        this.index = index;
    }
}

class LazySegTree<T, U>
{
    public int Count { get; }
    
    int n_layer;
    int[] segsize;
    T[][] data;    
    bool[][] lazy;
    U[][] lazyData;

    MergeFunction<T> merge;
    ResolveFunction<T, U> resolve;
    
    public LazySegTree(int N, MergeFunction<T> merge, ResolveFunction<T, U> resolve, T fill=default(T))
    {
        Count=N;

        this.merge=merge;
        this.resolve=resolve;
        
        n_layer=1;
        for(int k=1; k<N; k<<=1) n_layer+=1;

        segsize = new int[n_layer];
        data = new T[n_layer][];
        lazy = new bool[n_layer][];
        lazyData = new U[n_layer][];
        for(int l=0; l<n_layer; ++l) {
            segsize[l] = 1<<(n_layer-1-l);
            data[l] = new T[1<<l];
            lazy[l] = new bool[1<<l];
            lazyData[l] = new U[1<<l];
            for(int j=0; j<(1<<l); ++j) data[l][j]=fill;
        }
    }
    
    public T Resolve(int l, int index) {
        if(lazy[l][index]) {
            data[l][index] = resolve(data[l][index], lazyData[l][index], new STParams(layer: l, segsize: segsize[l], index: index));
            lazy[l][index] = false;
            if(l+1<n_layer) {
                lazyData[l+1][index*2] = lazyData[l+1][index*2+1] = lazyData[l][index];                
                lazy[l+1][index*2] = lazy[l+1][index*2+1] = true;                
            }
        }
        return data[l][index];
    }
    
    public T Query(int ibgn, int iend, int l=0) {
        int ssize = segsize[l];
        int index = ibgn/ssize;

        Resolve(l, index);

        if(ibgn%ssize==0 && iend-ibgn==ssize) return data[l][index];

        int imid = ibgn - ibgn%ssize + ssize/2;
        if(iend<=imid || imid<=ibgn) return Query(ibgn, iend, l+1);
        return merge(Query(ibgn, imid, l+1),
                     Query(imid, iend, l+1),
                     new STParams(layer: l, segsize: ssize, index: index));
    }
    
    public void Update(int ibgn, int iend, U value, int l=0) {
        int ssize = segsize[l];
        int index = ibgn/ssize;

        Resolve(l, index);
        
        if(ibgn%ssize==0 && iend-ibgn==ssize) {
            if(l+1<n_layer){
                lazyData[l+1][index*2] = lazyData[l+1][index*2+1] = value;
                lazy[l+1][index*2] = lazy[l+1][index*2+1] = true;
            }
            data[l][index] = resolve(data[l][index], value, new STParams(layer: l, segsize: ssize, index: index));
        }else{
            int imid = ibgn - ibgn%ssize + ssize/2;
            if(iend<=imid || imid<=ibgn){
                Update(ibgn, iend, value, l+1);
            } else {
                Update(ibgn, imid, value, l+1);
                Update(imid, iend, value, l+1);
            }
            data[l][index] = merge(Resolve(l+1, index*2), Resolve(l+1, index*2+1), new STParams(layer: l, segsize: ssize, index: index));
        }
    }
    

    public void Print()
    {
        Console.WriteLine($"Count   : {Count}");
        Console.WriteLine($"n_layer : {n_layer}");
        for(int l=0; l<n_layer; ++l) {
            var items = new String[data[l].Length];
            for(int i=0; i<data[l].Length; ++i) {
                items[i] = lazy[l][i] ? $"{data[l][i]}({lazyData[l][i]})" : $"{data[l][i]}";
            }
            Console.WriteLine($"[{l}] "+string.Join(" ", items));
        }
    }
}

class Program
{
    static long mod = 998244353;
    static long[] S;
    
    static long merge(long x, long y, STParams p) { return (x+y)%mod; }
    static long resolve(long value, long lazyValue, STParams p) {
        var ibgn = p.index*p.segsize;
        var iend = ibgn+p.segsize;
        return lazyValue*(S[iend]-S[ibgn]+mod)%mod;
    }
    
    static void Main()
    {
        var str = Console.ReadLine().Split(' ');
        int N = int.Parse(str[0]), Q = int.Parse(str[1]);
        
        S = new long[N+1];
        for(int i=0; i<N; ++i) S[i+1] = (S[i]*10+1)%mod;
        
        var st = new LazySegTree<long, long>(N, merge, resolve);
        st.Update(0, N, 1);

        for(int q=0; q<Q; ++q) {
            str = Console.ReadLine().Split(' ');
            int L = int.Parse(str[0]), R = int.Parse(str[1]), D = int.Parse(str[2]);
            st.Update(N-R, N-L+1, D);
            Console.WriteLine(st.Query(0, N));
        }
    }
}
