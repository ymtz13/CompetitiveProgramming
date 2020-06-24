using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        string[] buf;
        buf = Console.ReadLine().Split(new char[]{' '});
        var N = int.Parse(buf[0]);
        var D = int.Parse(buf[1]);
        
        buf = Console.ReadLine().Split(new char[]{' '});
        var X = int.Parse(buf[0]);
        var Y = int.Parse(buf[1]);

        if(X%D!=0 || Y%D!=0) { Console.WriteLine(0); return; }

        X/=D; Y/=D;

        var probList = new List<double>();
        for(int px=X; px<=N; ++px) {
            int mx = px-X;
            int Nx = px + mx;
            int Ny = N - Nx;
            if(Ny<0) break;
            int py = (Ny+Y)/2;
            int my = Ny - py;
            if(px+mx+py+my==N && py-my==Y && my>=0) {
                // prob = Comb(N, px) * Comb(N-px, mx) * Comb(Ny, py) / 4^N
                double prob = 1.0;
                int n = 0;
                for(int i=0; i<px; ++i) {
                    prob *= (double)(N-i)/(px-i);
                    while(prob>1 && n<N) { prob/=4.0; ++n; }
                }
                for(int i=0; i<mx; ++i) {
                    prob *= (double)(N-px-i)/(mx-i);
                    while(prob>1 && n<N) { prob/=4.0; ++n; }
                }
                for(int i=0; i<py; ++i) {
                    prob *= (double)(Ny-i)/(py-i);
                    while(prob>1 && n<N) { prob/=4.0; ++n; }
                }
                while(n<N) { prob/=4.0; ++n; }

                probList.Add(prob);
                //Console.WriteLine($"{px} {mx} {py} {my} {prob}");
            }
            
        }

        probList.Sort();
        double ans = 0;
        foreach(var prob in probList) ans += prob;
        
        Console.WriteLine(ans);
        
    }
}
