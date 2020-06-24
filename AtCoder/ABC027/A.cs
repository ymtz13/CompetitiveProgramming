using System;

class Program
{
    static void Main()
    {
        var str = Console.ReadLine().Split(new char[] {' '});
        string ans="";
        if (str[0]==str[1]) ans = str[2];
        if (str[1]==str[2]) ans = str[0];
        if (str[2]==str[0]) ans = str[1];
        Console.WriteLine(ans);

    }
}
