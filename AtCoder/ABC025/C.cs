using System;

class Program
{
    static int[,] B, C;
    static int[,] X;

    static int score() {
        int retval=0;
        for(int i=0; i<2; ++i)
            for(int j=0; j<3; ++j) if(X[i,j]==X[i+1,j]) retval += B[i,j];
                                                        
        for(int i=0; i<3; ++i)
            for(int j=0; j<2; ++j) if(X[i,j]==X[i,j+1]) retval += C[i,j];
        return retval;
    }

    static int dfs(int turn) {
        //Console.WriteLine(turn);
        if(turn==9) return score();
        
        int sign = 1-2*(turn%2);
        int max = -100000;
        for(int ij=0; ij<9; ++ij) {
            int i=ij/3, j=ij%3;
            if (X[i,j]!=0) continue;
            X[i,j] = sign;
            max = Math.Max(max, sign*dfs(turn+1));
            X[i,j] = 0;
        }

        return sign*max;
    }
    
    static void Main()
    {
        int sum=0;
        
        B = new int[2,3];
        for(int i=0; i<2; ++i) {
            var s = Console.ReadLine().Split(new char[] {' '});
            for(int j=0; j<3; ++j) { B[i,j] = int.Parse(s[j]); sum+=B[i,j]; }
        }
        
        C = new int[3,2];
        for(int i=0; i<3; ++i) {
            var s = Console.ReadLine().Split(new char[] {' '});
            for(int j=0; j<2; ++j) { C[i,j] = int.Parse(s[j]); sum+=C[i,j]; }
        }

        X = new int[3,3];
        int sc = dfs(0);
        Console.WriteLine(sc);
        Console.WriteLine(sum-sc);
    }

}
