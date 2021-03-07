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


class Program
{
    static void Main()
    {
        var str = Console.ReadLine().Split(" ");
        var N = int.Parse(str[0]);
        var Q = int.Parse(str[1]);

        var C = new int[N];
        str = Console.ReadLine().Split(" ");
        for(int i=0; i<N; ++i) C[i] = int.Parse(str[i]);
        
        var LR = new List<List<int>>();
        for(int q=0; q<Q; ++q) {
            str = Console.ReadLine().Split(" ");
            int l = int.Parse(str[0]);
            int r = int.Parse(str[1]);

            LR.Add(new List<int>{q, l, r});
        }

        LR.Sort((x, y) => x[2]-y[2]);

        var I = new int[N+1];
        for(int i=0; i<I.Length; ++i) I[i] = -1;
        
        var st = new SegTree<int>(N, (x, y) => x+y, 0);

        var ans = new int[Q];
        int j = 0;
        for(int iq=0; iq<Q; ++iq) {
            int q = LR[iq][0];
            int l = LR[iq][1];
            int r = LR[iq][2];

            for(; j<r; ++j) {
                int c = C[j];

                int iprev = I[c];
                I[c] = j;

                if(iprev!=-1) st.Update(iprev, 0);
                st.Update(j, 1);
            }
            ans[q] = st.Query(l-1,r);
        }

        Console.WriteLine(String.Join("\n", ans));
        
    }
}
