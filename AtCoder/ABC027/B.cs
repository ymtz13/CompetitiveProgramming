using System;

class Program
{
    static void Main()
    {
        var N = int.Parse(Console.ReadLine());
        var str = Console.ReadLine().Split(new char[] {' '});
        var A = new int[N];
        int S=0;
        for(int i=0; i<N; ++i) { A[i] = int.Parse(str[i]); S+=A[i]; }

        if(S%N>0) { Console.WriteLine(-1); return; }

        int M = S/N, m=0, ans=0;
        for(int i=0; i<N-1; ++i) {
            m += A[i]-M;
            if(m!=0) {++ans; }
        }

        Console.WriteLine(ans);
        

    }
}
