using System;

class Program
{
    static int Solve()
    {
        var N = int.Parse(Console.ReadLine());
        var S = Console.ReadLine();

        if(N%2==0) return -1;
        
        int M = (N-1)/2;
        var T = new char[N];
        T[M] = 'b';
        string Cl = "acb", Cr = "cab";
        for(int i=0; i<M; ++i) {
            T[M-i-1] = Cl[i%3];
            T[M+i+1] = Cr[i%3];
        }
        var U = new String(T);

        return (S==U ? M : -1);
        
    }
    
    static void Main()
    {
        Console.WriteLine(Solve());
    }
}
