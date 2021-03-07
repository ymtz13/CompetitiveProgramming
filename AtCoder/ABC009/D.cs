using System;

class Program
{
    static long[,] X;
    
    static public void Main()
    {
        string[] str;
        
        str = Console.ReadLine().Split(' ');
        long K = long.Parse(str[0]), M = long.Parse(str[1]);

        str = Console.ReadLine().Split(' ');
        var A = new long[K];
        for(int i=0; i<K; ++i) A[i] = long.Parse(str[i]);
        
        str = Console.ReadLine().Split(' ');
        var C = new long[K];
        for(int i=0; i<K; ++i) C[i] = long.Parse(str[i]);

        X = new long[K, K];
        for(int i=0; i<K; ++i) {
            for(int j=i; j<K; ++j) X[i,j] = C[K-1+i-j];
            for(int s=0; s<i; ++s) for(int j=0; j<K; ++j) X[i,j] ^= X[s,j] & C[i-s-1];
        }

        var N = (M-1)/K;
        for(; N>0; N>>=1) {
            if((N&1)>0) {
                var Anew = new long[K];
                for(int i=0; i<K; ++i) for(int j=0; j<K; ++j) Anew[i] ^= X[i,j] & A[j];
                A = Anew;
            }
            var Xnew = new long[K, K];
            for(int i=0; i<K; ++i)
            for(int j=0; j<K; ++j)
            for(int l=0; l<K; ++l)
                Xnew[i,l] ^= X[i,j] & X[j,l];
            X = Xnew;
        }

        Console.WriteLine(A[(M-1)%K]);
    }
}
