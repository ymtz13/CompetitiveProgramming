using System;

class Program
{
    static void Main()
    {
        string[] tmp;
        tmp = Console.ReadLine().Split(new char[]{' '});
        var N = int.Parse(tmp[0]);
        var M = int.Parse(tmp[1]);
        var D = int.Parse(tmp[2]);

        var map = new int[N];
        var loc = new int[N];
        for(int i=0; i<N; ++i) map[i] = loc[i] = i;
        
        tmp = Console.ReadLine().Split(new char[]{' '});
        for(int i=M-1; i>=0; --i) {
            var A = int.Parse(tmp[i]);
            map[A-1] ^= map[A];
            map[A]   ^= map[A-1];
            map[A-1] ^= map[A];
        }


        for(; D>0; D>>=1) {
            if((D&1)==1) {
                var loc_new = new int[N];
                for(int i=0; i<N; ++i) loc_new[map[i]] = loc[i];
                loc = loc_new;
            }

            var map_new = new int[N];
            for(int i=0; i<N; ++i) map_new[i] = map[map[i]];
            map = map_new;
        }

        var ans = new int[N];
        for(int i=0; i<N; ++i) ans[loc[i]] = i;

        for(int i=0; i<N; ++i) Console.WriteLine(ans[i]+1);

    }
}
