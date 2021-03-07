using System;

// 1 3 5 7 9 11 13 15 17  81
// (1 3 5) (7 9 11) (13 15 17)  81
// 1

// 1 3 5 7 9 11 = 36

class Program
{
    
    public static void Main()
    {
        var N = int.Parse(Console.ReadLine());
        int M;
        
        for(int p=2; p<N && M==0; ++p) {
            if(N%p==0) M = p;
        }

        if(M==0) {
            Console.WriteLine("impossible");
            return;
        }

        Console.WriteLine(M);
        for(int m=0; m<M; ++m) {
            for(int i=0; i<)
        }
        
    }
}
