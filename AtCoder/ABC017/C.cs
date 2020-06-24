using System;

class Program
{
    static void Main()
    {
        string[] buf;
        buf = Console.ReadLine().Split(new char[]{' '});
        var N = int.Parse(buf[0]);
        var M = int.Parse(buf[1]);

        var X = new long[M+1];
        long ans=0;
        for(int i=0; i<N; ++i) {
            buf = Console.ReadLine().Split(new char[]{' '});
            var l = int.Parse(buf[0]);
            var r = int.Parse(buf[1]);
            var s = int.Parse(buf[2]);
            X[l-1]+=s;
            X[r  ]-=s;
            ans+=s;
        }

        long d=0, dmin=X[0];
        for(int i=0; i<M; ++i) {
            d+=X[i];
            dmin = Math.Min(dmin, d);
        }

        Console.WriteLine(ans-dmin);
    }
}
