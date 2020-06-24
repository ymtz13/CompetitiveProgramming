using System;

class Program
{
    static void Main()
    {
        string[] str = Console.ReadLine().Split(new char[]{' '});
        int n = int.Parse(str[0]), m = int.Parse(str[1]);

        double s=(n%12)*30.0+m/2.0, l=m*6.0;
        double deg = Math.Max(s,l)-Math.Min(s,l);
        Console.WriteLine(Math.Min(deg, 360.0-deg));
    }

}
