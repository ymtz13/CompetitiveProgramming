using System;

class Program
{
    static long pow(long x, long k, long mod)
    {
        long r = 1;
        while(k>0) {
            if((k&1)==1) r=(r*x)%mod;
            x=x*x%mod;
            k>>=1;
        }
        return r;
    }
    
    static void Main()
    {
        long A = long.Parse(Console.ReadLine());
        long B = long.Parse(Console.ReadLine());
        long C = long.Parse(Console.ReadLine());

        long mod = 1000000007;

        long Ainv = pow(A, mod-2, mod);
        long S = ( C * Ainv + mod - 1 ) % mod;
        long T = ( B * Ainv + mod - 1 ) % mod;
        long U = ( 1 + (mod-S)*T ) % mod;

        long r = (S*T+T)%mod * pow(U, mod-2, mod) % mod;
        long c = (r+1)*S%mod;
               
        Console.WriteLine("{0} {1}", r, c);

    }



}
