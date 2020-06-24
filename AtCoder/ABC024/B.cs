using System;

class Program
{
    static void Main()
    {
        var s = Console.ReadLine().Split(new char[]{' '});
        int N = int.Parse(s[0]),
            T = int.Parse(s[1]);

        int ans=0, t=0;
        for(int i=0; i<N; ++i) {
            int A = int.Parse(Console.ReadLine());
            ans+=T;
            if(A<t) ans-=t-A;
            t=A+T;
        }

        Console.WriteLine(ans);

    }


}
