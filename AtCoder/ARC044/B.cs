using System;

class Combination
{
    static public long Power(long x, long k, long mod) {
        long retval = 1;
        for(; k>0; k>>=1) {
            if((k&1)==1) retval = retval * x % mod;
            x = x * x % mod;
        }
        return retval;
    }
}

class Program
{
    static long Solve()
    {
        const long mod = 1000000007;
        
        var N = int.Parse(Console.ReadLine());

        string[] str = Console.ReadLine().Split(' ');
        var A = new int[N];
        for(int i=0; i<N; ++i) A[i] = int.Parse(str[i]);

        if(A[0]!=0) return 0;
        
        var K = new long[N];
        K[0] = 1;
        for(int i=1; i<N; ++i) {
            var a = A[i];
            if(a==0) return 0;
            ++K[a];
        }

        long ans = 1;
        for(int i=1; i<N; ++i) {
            var p = K[i];
            var q = K[i-1];

            var x = (Combination.Power(2, q, mod) + mod-1) % mod;
            ans = ans * Combination.Power(x, p, mod) % mod;

            ans = ans * Combination.Power(2, p*(p-1)/2, mod) % mod;
        }

        return ans;
    }
    
    public static void Main()
    {
        Console.WriteLine(Solve());
    }

}
