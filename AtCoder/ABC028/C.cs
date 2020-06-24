using System;
using System.Collections.Generic;

class Program
{
    static List<int> L;
    static List<int> X;
    
    static void Main()
    {
        L = new List<int>();
        
        var str = Console.ReadLine().Split(" ");
        X = new List<int>();
        for(int i=0; i<5; ++i) X.Add(int.Parse(str[i]));
        
        Dfs(0, 0, 0);

        L.Sort();
        Console.WriteLine(L[L.Count-3]);

    }

    static void Dfs(int i, int n, int s)
    {
        if(n==3) L.Add(s);
        if(i==5) return;

        Dfs(i+1, n+1, s+X[i]);
        Dfs(i+1, n  , s     );
    }
}
