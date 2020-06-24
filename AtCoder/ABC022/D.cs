using System;

class Program
{
    static double MaxDistFromGOM(int N)
    {
        var X = new int[N];
        var Y = new int[N];
        double Gx = 0, Gy = 0;
        for(int i=0; i<N; ++i) {
            var s = Console.ReadLine().Split(new char[]{' '});
            var x = int.Parse(s[0]);
            var y = int.Parse(s[1]);
            X[i] = x;
            Y[i] = y;
            Gx += x;
            Gy += y;
        }
        Gx /= N;
        Gy /= N;

        double dmax = 0;
        for(int i=0; i<N; ++i) {
            var x = X[i];
            var y = Y[i];
            double dx = Gx-x;
            double dy = Gy-y;
            double d = Math.Sqrt(dx*dx+dy*dy);
            dmax = Math.Max(dmax, d);
        }
        
        return dmax;
    }
    
    static void Main()
    {
        var N = int.Parse(Console.ReadLine());

        double dA = MaxDistFromGOM(N);
        double dB = MaxDistFromGOM(N);
        
        Console.WriteLine(dB/dA);
    }

}
