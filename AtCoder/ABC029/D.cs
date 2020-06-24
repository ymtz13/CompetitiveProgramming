using System;

class Program
{
    static void Main()
    {
        var N = long.Parse(Console.ReadLine());

        long d=1, ans=0;
        while(d<=N) {
            ans += N/(d*10)*d;
            if((N/d)%10==1) ans += N%d+1;
            if((N/d)%10>=2) ans += d;
            d*=10;
        }

        Console.WriteLine(ans);

    }
}
