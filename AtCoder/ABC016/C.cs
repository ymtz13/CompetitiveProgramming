using System;

class Program
{
    static void Main()
    {
        string[] buf;
        buf = Console.ReadLine().Split(" ");
        var N = int.Parse(buf[0]);
        var M = int.Parse(buf[1]);
        var E = new bool[N,N];

        for(int m=0; m<M; ++m) {
            buf = Console.ReadLine().Split(" ");
            var A = int.Parse(buf[1]);
            var B = int.Parse(buf[0]);
            E[A-1,B-1] = E[B-1,A-1] = true;
        }
        
        for(int i=0; i<N; ++i) {
            int ans = 0;
            for(int j=0; j<N; ++j) {
                if(i==j || E[i,j]) continue;
                for(int k=0; k<N; ++k) if(E[i,k]&&E[k,j]) {++ans; break;}
            }
            Console.WriteLine(ans);
        }
        
    }
}
