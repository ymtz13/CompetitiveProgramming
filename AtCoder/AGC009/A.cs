using System;

class Program
{
    public static void Main()
    {
        var N = int.Parse(Console.ReadLine());

        var A = new long[N];
        var B = new long[N];
        
        string[] str;

        for(int i=0; i<N; ++i) {
            str = Console.ReadLine().Split(' ');
            A[i] = long.Parse(str[0]);
            B[i] = long.Parse(str[1]);
        }

        long K = 0;
        for(int i=N-1; i>=0; --i) {
            var k = B[i] - (A[i] + K) % B[i];
            if(k==B[i]) k=0;
            K+=k;
        }
        Console.WriteLine(K);
    }
}
