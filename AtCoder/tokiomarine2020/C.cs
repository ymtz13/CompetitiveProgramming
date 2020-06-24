using System;
using System.Linq;

class Program
{
    static void Main()
    {
        var NK = Console.ReadLine().Split().Select(int.Parse).ToArray();
        int N = NK[0], K = NK[1];

        var A = Console.ReadLine().Split().Select(int.Parse).ToArray();

        for(int k=0; k<K; ++k) {
            var B = new int[N+1];
            for(int i=0; i<N; ++i) {
                int a = A[i];
                B[Math.Max(0, i-a  )]++;
                B[Math.Min(N, i+a+1)]--;
            }
            int v = 0;
            bool exist_not_N = false;
            for(int i=0; i<N; ++i) {
                v += B[i];
                A[i] = v;
                exist_not_N = exist_not_N || (v!=N);
            }
            if(!exist_not_N) break;
        }

        Console.WriteLine(string.Join(" ", A));
    }
}
