using System;

class Program
{
    static void Main()
    {
        int ans = 0;
        for(int i=0; i<12; ++i) {
            if (Console.ReadLine().Contains("r")) ++ans;
        }
        Console.WriteLine(ans);

    }

}
