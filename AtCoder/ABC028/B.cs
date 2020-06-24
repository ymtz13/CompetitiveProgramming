using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        var S = Console.ReadLine();
        var D = new Dictionary<char, int>();
        var C = new char[] {'A','B','C','D','E','F'};
        foreach(var c in C) D.Add(c, 0);

        for(int i=0; i<S.Length; ++i) ++D[S[i]];

        var ans = new int[6];
        for(int i=0; i<C.Length; ++i) ans[i] = D[C[i]];

        Console.WriteLine(string.Join(" ", ans));
    }
}
