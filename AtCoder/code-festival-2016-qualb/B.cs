using System;

class Program
{
    public static void Main()
    {
        var str = Console.ReadLine().Split(' ');
        int N = int.Parse(str[0]);
        int A = int.Parse(str[1]);
        int B = int.Parse(str[2]);
        int X = 0, Y = 0;

        var S = Console.ReadLine();
        for(int i=0; i<N; ++i) {
            var c = S[i];
            if(c=='a' && X<A+B) {
                Console.WriteLine("Yes");
                ++X;
                continue;
            }
            if(c=='b' && X<A+B && Y<B) {
                Console.WriteLine("Yes");
                ++X;
                ++Y;
                continue;
            }
            Console.WriteLine("No");
        }
    }
}
