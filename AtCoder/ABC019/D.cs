using System;

class Program
{
    static void Main()
    {
        var N = int.Parse(Console.ReadLine());

        int dmax = 0, vmax=2;
        for(int v=2; v<=N; ++v) {
            Console.WriteLine("? 1 {0}", v);
            var d = int.Parse(Console.ReadLine());
            if(dmax<d) { dmax=d; vmax=v; }
        }

        for(int v=1; v<=N; ++v) {
            if(v==vmax) continue; 
            Console.WriteLine("? {0} {1}", vmax, v);
            var d = int.Parse(Console.ReadLine());
            if(dmax<d) { dmax=d; }
        }

        Console.WriteLine("! {0}", dmax);
            
    }
}
