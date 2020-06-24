using System;

class Program
{
    static void Main()
    {
        string[] str1 = Console.ReadLine().Split(new char[]{' '});
        int N = int.Parse(str1[0]), M = int.Parse(str1[1]);
        
        string[] str2 = Console.ReadLine().Split(new char[]{' '});
        int X = int.Parse(str2[0]), Y = int.Parse(str2[1]);

        string[] As = Console.ReadLine().Split(new char[]{' '});
        string[] Bs = Console.ReadLine().Split(new char[]{' '});

        int[] A = new int[N];
        int[] B = new int[M];

        for(int i=0; i<N; ++i) A[i] = int.Parse(As[i]);
        for(int i=0; i<M; ++i) B[i] = int.Parse(Bs[i]);
        
        int ans=0, ia=0, ib=0, t=0;
        while(true) {
            while(ia<N && A[ia]<t) ++ia;
            if(ia==N) break;
            t = A[ia]+X;
            
            while(ib<M && B[ib]<t) ++ib;
            if(ib==M) break;
            t = B[ib]+Y;

            ++ans;
        }

        Console.WriteLine(ans);

    }

}
