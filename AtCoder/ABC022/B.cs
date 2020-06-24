using System;

class Program
{
    static void Main()
    {
        var N = int.Parse(Console.ReadLine());
        var F = new bool[100001];
        int ans = 0;
        for(int i=0; i<N; ++i) {
            var A = int.Parse(Console.ReadLine());
            if(F[A]) ++ans;
            F[A]=true;
        }

        Console.WriteLine(ans);
    }
}
