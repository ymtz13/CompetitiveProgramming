using System;

class Program
{
    static void Main()
    {
        string[] str = Console.ReadLine().Split(new char[] {' '});
        int A = int.Parse(str[0]);
        int B = int.Parse(str[1]);
        int C = int.Parse(str[2]);
        int D = int.Parse(str[3]);

        int rhs = B*C, lhs = A*D;
        
        Console.WriteLine(rhs>lhs ? "TAKAHASHI" : (rhs<lhs ? "AOKI" : "DRAW"));
    }
}
