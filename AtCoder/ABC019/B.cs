using System;

class Program
{
    static void Main()
    {
        var s = Console.ReadLine()+"_";

        int n=0;
        string ans="";
        for(int i=0; i<s.Length-1; ++i) {
            ++n;
            if(s[i]!=s[i+1]) { ans+=string.Format("{0}{1}", s[i], n); n=0; }
        }

        Console.WriteLine(ans);
    }
}
