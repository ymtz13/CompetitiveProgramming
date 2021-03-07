using System;

class Program
{
    public static void Main() {
        int ans = 0;
        var S = Console.ReadLine();
        for(int i=0; i<16; ++i) if(S[i]!="CODEFESTIVAL2016"[i]) ++ans;
        Console.WriteLine(ans);
    }
}
