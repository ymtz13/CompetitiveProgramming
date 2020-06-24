using System;

class Program
{
    static void Main()
    {
        var str = Console.ReadLine().Split(new char[] {' '});
        long N = long.Parse(str[0]), K = long.Parse(str[1]);

        double p = 1 + (N-1)*3 + (K-1)*(N-K)*6;
        double q = N*N*N;
        Console.WriteLine(p/q);

    }
}
