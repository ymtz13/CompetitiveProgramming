using System;

class Program
{
    static void Main()
    {
        int W = int.Parse(Console.ReadLine());

        string[] buf;
        buf = Console.ReadLine().Split(new char[]{' '});
        var N = int.Parse(buf[0]);
        var K = int.Parse(buf[1]);

        var dp = new int[K+1,W+1];  
        for(int k=1; k<=K; ++k)
        for(int w=0; w<=W; ++w)
            dp[k,w]=-1;

        int ans = 0;
        for(int i=0; i<N; ++i) {
            buf = Console.ReadLine().Split(new char[]{' '});
            var A = int.Parse(buf[0]);
            var B = int.Parse(buf[1]);

            for(int k=K; k>0; --k) for(int w=A; w<=W; ++w) {
                if(dp[k-1,w-A]>=0) dp[k,w] = Math.Max(dp[k,w], dp[k-1,w-A]+B);
                ans = Math.Max(ans, dp[k,w]);
                }
        }
        Console.WriteLine(ans);
        
        
    }
}
