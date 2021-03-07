using System;
using System.Linq;

// 1 0 0
// 0 1 1

class Program
{
    public static void Main()
    {
        var N = int.Parse(Console.ReadLine());
        var A = Console.ReadLine().Split(' ').Select(long.Parse).ToList();
        var B = Console.ReadLine().Split(' ').Select(long.Parse).ToList();

        var Sa = A.Sum();
        var Sb = B.Sum();

        long n = 0;
        for(int i=0; i<N; ++i) {
            n += Math.Max(0, A[i]-B[i]);
        }

        Console.WriteLine(n<=Sb-Sa ? "Yes" : "No");
    }
}

