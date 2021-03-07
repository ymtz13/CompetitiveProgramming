using System;

class Combination
{
    static T Power<T>(T x, long k, long mod) {
        T retval = 1;
        for(; k>0; k>>=1) {
            if((k&1)==1) retval = retval * x % mod;
            x = x * x % mod;
        }
        return retval;
    }
}


class Program
{
    public static void Main()
    {
        Console.WriteLine($"Power(3,4,10000) = {Combination.Power(3,4,10000)}");
    }
}
