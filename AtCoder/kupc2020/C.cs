using System;

// abcdefghijklm
// bd
// bcdefghijklma
// opqrstuvwxyzn


class Program
{
    public static void Main()
    {
        string[] s = {"abcdefghijklm", "nopqrstuvwxyz"};

        var ans = new string[13];
        for(int i=0; i<12; ++i) {
            string r = "";
            for(int j=0; j<13; ++j) r += s[i%2][(i+j*(i+1))%13];
            ans[i] = r;
        }
        ans[12] = s[1];

        for(int i=0; i<13; ++i) Console.WriteLine(ans[i]);

    }
}
