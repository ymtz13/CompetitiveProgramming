using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        var RCK = Console.ReadLine().Split(new char[]{' '});
        int R = int.Parse(RCK[0]),
            C = int.Parse(RCK[1]),
            K = int.Parse(RCK[2]);

        var S = new int[R+2,C+2];
        for(int c=0; c<C+2; ++c) S[0,c]=S[R+1,c]=1;
        for(int r=1; r<R+1; ++r) {
            var s = Console.ReadLine();
            S[r,0]=S[r,C+1]=1;
            for(int c=1; c<C+1; ++c) if(s[c-1]=='x') S[r,c]=1;
        }

        int ans = (R+2)*(C+2);
        var queue = new List<int[]>();
        for(int r=0; r<R+2; ++r)
        for(int c=0; c<C+2; ++c)
            if(S[r,c]==1) { queue.Add(new int[]{r,c}); --ans; }

        var dx = new int[]{+1,-1, 0, 0};
        var dy = new int[]{ 0, 0,+1,-1};

        for(int k=0; k<K-1; ++k) {
            var queue_new = new List<int[]>();
            foreach(var q in queue) {
                var qx = q[0];
                var qy = q[1];
                for(int i=0; i<4; ++i) {
                    var tx = qx+dx[i];
                    var ty = qy+dy[i];
                    if(tx<0 || tx>R+1 || ty<0 || ty>C+1) continue;
                    if(S[tx,ty]==0) {
                        S[tx,ty]=1;
                        queue_new.Add(new int[]{tx, ty});
                        --ans;
                    }
                }
            }
            queue=queue_new;
        }

        Console.WriteLine(ans);
        
    }
}
