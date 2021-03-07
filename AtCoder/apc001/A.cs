using System;
using System.Linq;

class Program
{
    public static void Main()
    {
        var XY = Console.ReadLine().Split(' ').Select(int.Parse).ToList();
        int X = XY[0], Y = XY[1];
        Console.WriteLine(X%Y==0 ? -1 : X);
    }
}
