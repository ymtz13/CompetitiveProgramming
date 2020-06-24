using System;

class Program
{
    static void Main()
    {
        var N = long.Parse(Console.ReadLine());

        long p=2*N+1, q=N+1;
        while(true) {
            if(q<=1 && 1<=p) { Console.WriteLine("Takahashi"); return; }
            // 2*N+1 <= p    N<=(p-1)/2
            // 2*N   >= q    N>=q/2
            p = (p-1)/2;
            q = (q+1)/2;
            
            if(q<=1 && 1<=p) { Console.WriteLine("Aoki"); return; }
            // 2*N   <= p    N<=p/2
            // 2*N+1 >= q    N>=(q-1)/2
            p = p/2;
            q = q/2;

        }

    }

}
