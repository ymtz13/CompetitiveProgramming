using System;

class Program
{
    static void Main()
    {
        var s = Console.ReadLine().Split(new char[]{' '});
        int N = int.Parse(s[0]),
            A = int.Parse(s[1]),
            B = int.Parse(s[2]),
            X = 0;

        for(int i=0; i<N; ++i) {
            var sd = Console.ReadLine().Split(new char[]{' '});
            int d = int.Parse(sd[1]);
            d = Math.Max(d, A);
            d = Math.Min(d, B);
            X += (sd[0]=="East" ? d : -d); 
        }

        if(X==0) Console.WriteLine(0);
        if(X> 0) Console.WriteLine("East {0}", X);
        if(X< 0) Console.WriteLine("West {0}",-X);
    }

}
