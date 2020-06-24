using System;

class Program
{
    static void Main()
    {
        var N = int.Parse(Console.ReadLine());
        var H = new int[N];
        var S = new int[N];

        for(int i=0; i<N; ++i) {
            var s = Console.ReadLine().Split(new char[]{' '});
            H[i] = int.Parse(s[0]);
            S[i] = int.Parse(s[1]);
        }

        long min_ok = 200000000000000, max_ng = 0;
        while(min_ok-max_ng>1) {
            long tgt = (min_ok+max_ng)/2;
            bool ok=true;

            var T = new int[N];
            for(int i=0; i<N; ++i) {
                // H+St<=tgt
                // t<=(tgt-H)/S
                if(tgt<H[i]) { ok=false; break; }
                ++T[Math.Min(N-1, (tgt-H[i])/S[i])];
            }
            
            int r=0;
            for(int t=0; t<N && ok; ++t) {
                r+=T[t];
                if(r>t+1) ok=false;
            }

            if(ok) { min_ok=tgt; } else { max_ng=tgt; }
        }

        Console.WriteLine(min_ok);
        
    }
}
