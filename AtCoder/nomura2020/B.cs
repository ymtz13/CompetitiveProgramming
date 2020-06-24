using System;
using System.Collections.Generic;

class Program
{
    static char[] T;
    static List<int> LQ;

    static int[,] memo;
    
    static int Score(int i)
    {
        if(i==LQ.Count)
    }
    
    static void Main()
    {
        var tmp = Console.ReadLine();
        T = new char[tmp.Length+2];
        T[0]='?';
        T[1]='_';
        LQ.Add(0);
        for(int i=0; i<tmp.Length; ++i) {
            T[i+2] = tmp[i];
            if(tmp[i]=='?') LQ.Add(i+2);
        }
                              
        Console.WriteLine();
    }
}
