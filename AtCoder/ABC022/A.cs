using System;

class Program
{
    static void Main()
    {
        var s = Console.ReadLine().Split(new char[]{' '});
        int N = int.Parse(s[0]),
            S = int.Parse(s[1]),
            T = int.Parse(s[2]);
        
        var W = int.Parse(Console.ReadLine());
        int ans = 0;
        if(S<=W && W<=T) ++ans;
        for(int i=0; i<N-1; ++i) {
            W += int.Parse(Console.ReadLine());
            if(S<=W && W<=T) ++ans;
        }
        Console.WriteLine(ans);
        
    }
}
