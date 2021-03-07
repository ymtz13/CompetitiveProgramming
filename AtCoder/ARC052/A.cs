using System;

class Program
{
    public static void Main()
    {
        var S = Console.ReadLine();
        long ans = 0;
        for(int i=0; i<S.Length; ++i) {
            var c = S[i];
            if((int)'0' <= (int)c && (int)c <= (int)'9') {
                if(ans>0) ans*=10;
                ans += ((int)c - (int)'0');
            }
        }
        Console.WriteLine(ans);
    }
}
