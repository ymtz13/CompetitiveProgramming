using System;

class Program
{
    static void Main()
    {
        var s1 = Console.ReadLine().Split(new char[]{' '});
        int N = int.Parse(s1[0]),
            D = int.Parse(s1[1]),
            K = int.Parse(s1[2]);

        var LR = new int[D, 2];
        for(int d=0; d<D; ++d) {
            var s2 = Console.ReadLine().Split(new char[]{' '});
            LR[d,0] = int.Parse(s2[0]);
            LR[d,1] = int.Parse(s2[1]);
        }

        for(int k=0; k<K; ++k) {
            var s2 = Console.ReadLine().Split(new char[]{' '});
            var S = int.Parse(s2[0]);
            var T = int.Parse(s2[1]);

            for(int d=0; d<D; ++d) {
                var L = LR[d,0];
                var R = LR[d,1];
                if(L<=S && S<=R) {
                    if(S<T) {S=Math.Min(T,R);} else {S=Math.Max(T,L);}
                }
                if(S==T){ Console.WriteLine(d+1); break; }
            }
        }


    }
}
