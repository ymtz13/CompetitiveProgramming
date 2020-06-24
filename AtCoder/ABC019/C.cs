using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        var N = int.Parse(Console.ReadLine());
        var buf = Console.ReadLine().Split(new char[]{' '});

        var S = new SortedSet<long>();
        int ans = 0;
        for(int i=0; i<N; ++i) {
            var a = long.Parse(buf[i]);
            if(!S.Contains(a)) ++ans;
            var _a = a;
            while(a<=1000000000) {S.Add(a); a*=2;}
            while(_a%2==0) {_a/=2; S.Add(_a);}
        }

        Console.WriteLine(ans);
        
    }
}
