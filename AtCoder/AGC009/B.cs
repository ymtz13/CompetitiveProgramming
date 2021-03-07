using System;
using System.Collections.Generic;

class Program
{
    static List<int>[] A;

    static int Dfs(int x) {
        var B = new List<int>();
        var L = A[x].Count;
        
        for(int i=0; i<L; ++i) B.Add(Dfs(A[x][i]));
        B.Sort();

        int retval = 0;
        for(int i=0; i<L; ++i) retval = Math.Max(retval, B[i]+L-i);
        
        return retval;
    }
    
    static public void Main()
    {
        var N = int.Parse(Console.ReadLine());

        A = new List<int>[N+1];
        for(int i=0; i<=N; ++i) A[i] = new List<int>();

        for(int i=2; i<=N; ++i) A[int.Parse(Console.ReadLine())].Add(i);

        Console.WriteLine(Dfs(1));
    }
}
