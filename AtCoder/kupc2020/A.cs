using System;
using System.Linq;

class Program
{
    public static void Main()
    {
        var N = int.Parse(Console.ReadLine());
        var XY = Console.ReadLine().Split(' ').Select(int.Parse).ToList();

        int ans = 0;
        for(int i=0; i<N-1; ++i) {
            var xy = Console.ReadLine().Split(' ').Select(int.Parse).ToList();
            ans += Math.Abs(XY[0]-xy[0]) + Math.Abs(XY[1]-xy[1]);
            XY = xy;
        }

        Console.WriteLine(ans);
    }
}
