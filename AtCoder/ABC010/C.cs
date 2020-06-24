using System;

class Program
{
    static double Dist(int x1, int y1, int x2, int y2)
    {
        var dx = x1 - x2;
        var dy = y1 - y2;
        return Math.Sqrt(dx*dx+dy*dy);
    }
    
    static void Main()
    {
        string[] buf;
        buf = Console.ReadLine().Split(new char[]{' '});
        var xi = int.Parse(buf[0]);
        var yi = int.Parse(buf[1]);
        var xf = int.Parse(buf[2]);
        var yf = int.Parse(buf[3]);
        var T = int.Parse(buf[4]);
        var V = int.Parse(buf[5]);
        var D = T*V;

        var n = int.Parse(Console.ReadLine());

        var ans = "NO";
        for(int i=0; i<n; ++i) {
            buf = Console.ReadLine().Split(new char[]{' '});
            var x = int.Parse(buf[0]);
            var y = int.Parse(buf[1]);
            if(Dist(xi,yi, x,y) + Dist(xf,yf, x,y) <= D+1e-5) ans = "YES";
        }

        Console.WriteLine(ans);
        
    }
}
