using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        var S = Console.ReadLine();
        var L = new List<int>();

        int x = 0;
        for(int i=S.Length-1; i>=0; --i) {
            char c = S[i];
            if(c=='M') L.Add(x);
            if(c=='+') ++x;
            if(c=='-') --x;
        }

        L.Sort();

        long ans=0;
        int M=L.Count/2;
        for(int i=0; i<M; ++i) ans += L[i+M]-L[i];
        Console.WriteLine(ans);
    }
}
