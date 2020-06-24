using System;

class Program
{

    static int N, M, Q;
    static int[,] P;
    static int[] A;

    static int dfs(int i) {
        int score = 0;
        
        if(i==N+1) {
            for(int q=0; q<Q; ++q) {
                int a = P[q,0],
                    b = P[q,1],
                    c = P[q,2],
                    d = P[q,3];
                   
                if(A[b]-A[a]==c) score+=d;
            }
            return score;
        }

        for(int x=A[i-1]; x<=M; ++x) {
            A[i]=x;
            score = Math.Max(score, dfs(i+1));
        }
        return score;
    }
    
    static void Main()
    {
        string[] buf;
        
        buf = Console.ReadLine().Split(new char[]{' '});
        N = int.Parse(buf[0]);
        M = int.Parse(buf[1]);
        Q = int.Parse(buf[2]);

        P = new int[Q,4];
        for(int i=0; i<Q; ++i) {
            buf = Console.ReadLine().Split(new char[]{' '});
            for(int j=0; j<4; ++j) P[i,j] = int.Parse(buf[j]);
        }

        A = new int[N+1];
        A[0] = 1;
        Console.WriteLine(dfs(1));
        
    }
}
