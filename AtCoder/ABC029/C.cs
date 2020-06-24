using System;

class Program
{
    static int N;
    
    static void Main()
    {
        N = int.Parse(Console.ReadLine());

        Dfs(0, "");
    }

    static void Dfs(int i, string s)
    {
        if(i==N) { Console.WriteLine(s); return; }
        Dfs(i+1, s+"a");
        Dfs(i+1, s+"b");
        Dfs(i+1, s+"c");
    }

}
