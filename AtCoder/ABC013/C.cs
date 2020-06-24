using System;

class Program
{
    static void Main()
    {
        string[] buf;
        
        buf = Console.ReadLine().Split(new char[]{' '});
        var N = long.Parse(buf[0]);
        var H = long.Parse(buf[1]);
        
        buf = Console.ReadLine().Split(new char[]{' '});
        var A = long.Parse(buf[0]);
        var B = long.Parse(buf[1]);
        var C = long.Parse(buf[2]);
        var D = long.Parse(buf[3]);
        var E = long.Parse(buf[4]);

        long ans = C*N;
        for(long n=0; n<=N; ++n) {
            long Q = (N-n)*E - H + 1; // quantity to eat
            long X = Math.Max(0, (Q-n*D+B-D-1)/(B-D)); // num of normal foods   (4-2*4+4-1-1)/(4-1) = (-2)/(-3)
            if(X>n) continue;
            ans = Math.Min(ans, A*X+C*(n-X));
        }

        Console.WriteLine(ans);
        
    }
}
