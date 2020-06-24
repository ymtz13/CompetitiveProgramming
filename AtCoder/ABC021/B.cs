using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        var S = new SortedSet<int>();
        string[] buf;
        
        Console.ReadLine();
        buf = Console.ReadLine().Split(new char[]{' '});
        for(int i=0; i<buf.Length; ++i) S.Add(int.Parse(buf[i]));

        Console.ReadLine();
        buf = Console.ReadLine().Split(new char[]{' '});
        for(int i=0; i<buf.Length; ++i) S.Add(int.Parse(buf[i]));

        Console.WriteLine(S.Count==buf.Length+2?"YES":"NO");
        
    }
}
