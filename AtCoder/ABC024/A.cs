using System;

class Program
{
    static void Main()
    {
        var s1 = Console.ReadLine().Split(new char[]{' '});
        int A = int.Parse(s1[0]),
            B = int.Parse(s1[1]),
            C = int.Parse(s1[2]),
            K = int.Parse(s1[3]);
        
        var s2 = Console.ReadLine().Split(new char[]{' '});
        int S = int.Parse(s2[0]),
            T = int.Parse(s2[1]);

        int ans = S*A+T*B;
        if(S+T>=K) ans-=C*(S+T);
        Console.WriteLine(ans);

    }
}
