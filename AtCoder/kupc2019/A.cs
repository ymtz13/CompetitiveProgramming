using System;
using System.Linq;

class Program
{
    public static void Main()
    {
        var NX = Console.ReadLine().Split(' ').Select(int.Parse).ToList();
        int N = NX[0], X = NX[1];

        var A = Console.ReadLine().Split(' ').Select(int.Parse);
        var M = A.Max();
        
        int ans = 0;
        foreach(var a in A) {
            if(a+X>=M) ++ans;
        }

        Console.WriteLine(ans);
        
    }
}
