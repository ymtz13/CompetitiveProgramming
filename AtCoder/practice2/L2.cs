using System;

delegate T MergeFunction<T>(T v1, T v2, int layer, int segsize, int index);
delegate T ResolveFunction<T, U>(T value, U lazyValue, int layer, int segsize, int index);
delegate U PostponeFunction<U>(bool isLazy, U oldValue, U value, int layer, int segsize, int index);

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
    PostponeFunction<U> postpone;
    
    public LazySegTree(int N, MergeFunction<T> merge, ResolveFunction<T, U> resolve, PostponeFunction<U> postpone, T fill=default(T))
    {
        Count=N;

        this.merge=merge;
        this.resolve=resolve;
        this.postpone=postpone;
        
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
        }

        for(int j=0; j<data[n_layer-1].Length; ++j) data[n_layer-1][j]=fill;
        for(int l=n_layer-2; l>=0; --l) {
            for(int j=0; j<(1<<l); ++j)
                data[l][j] = merge(data[l+1][j*2], data[l+1][j*2+1], layer: l, segsize: segsize[l], index: j);
        }
    }

    public T Resolve(int l, int index) {
        if(lazy[l][index]) {
            data[l][index] = resolve(data[l][index], lazyData[l][index], layer: l, segsize: segsize[l], index: index);
            lazy[l][index] = false;
            if(l+1<n_layer) {
                lazyData[l+1][index*2  ] = postpone(lazy[l+1][index*2  ], lazyData[l+1][index*2  ], lazyData[l][index], layer: l+1, segsize: segsize[l+1], index: index*2  );
                lazyData[l+1][index*2+1] = postpone(lazy[l+1][index*2+1], lazyData[l+1][index*2+1], lazyData[l][index], layer: l+1, segsize: segsize[l+1], index: index*2+1);
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
                     layer: l, segsize: ssize, index: index);
    }
    
    public void Update(int ibgn, int iend, U value, int l=0) {
        int ssize = segsize[l];
        int index = ibgn/ssize;
                
        if(ibgn%ssize==0 && iend-ibgn==ssize) {
            lazyData[l][index] = postpone(lazy[l][index], lazyData[l][index], value, layer: l, segsize: ssize, index: index);
            lazy[l][index] = true;
            Resolve(l, index);
        }else{
            Resolve(l, index);
            
            int imid = ibgn - ibgn%ssize + ssize/2;
            if(iend<=imid || imid<=ibgn){
                Update(ibgn, iend, value, l+1);
            } else {
                Update(ibgn, imid, value, l+1);
                Update(imid, iend, value, l+1);
            }
            data[l][index] = merge(Resolve(l+1, index*2), Resolve(l+1, index*2+1), layer: l, segsize: ssize, index: index);
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

class Node {
    public long ninv, n0, n1;
    public Node(long ninv, long n0, long n1) {
        this.ninv = ninv;
        this.n0 = n0;
        this.n1 = n1;
    }
    public override string ToString() {
        return $"<{ninv},{n0},{n1}>";
    }
}

class Program
{
    static Node merge(Node l, Node r, int layer, int segsize, int index) {
        return new Node(l.ninv + r.ninv + l.n1*r.n0 ,l.n0 + r.n0, l.n1 + r.n1);
    }
    static Node resolve(Node v, int lazyValue, int layer, int segsize, int index) {
        return lazyValue%2==1 ? new Node(v.n0*v.n1-v.ninv ,v.n1, v.n0) : v;
    }
    static int postpone(bool isLazy, int oldValue, int value, int layer, int segsize, int index) {
        return isLazy ? oldValue + value : value;
    }
    
    static void Main()
    {
        string[] str;
        
        str = Console.ReadLine().Split(' ');
        int N = int.Parse(str[0]), Q = int.Parse(str[1]);

        var st = new LazySegTree<Node, int>(N, merge, resolve, postpone, new Node(0, 0, 1));

        str = Console.ReadLine().Split(' ');
        for(int i=0; i<N; ++i) {
            var A = int.Parse(str[i]);
            if(A==0) st.Update(i, i+1, 1);
        }

        for(int q=0; q<Q; ++q) {
            str = Console.ReadLine().Split(' ');
            int T = int.Parse(str[0]), L = int.Parse(str[1]), R = int.Parse(str[2]);
            if(T==1) {
                st.Update(L-1, R, 1);
            }else{
                Console.WriteLine(st.Query(L-1, R).ninv);
            }
        }
    }
}
