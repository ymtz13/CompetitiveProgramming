using System;

class Program
{
    static int H, W, T;
    static char[,] S;
    static int Sh, Sw, Gh, Gw;

    static int[] dx = { 0, 0, +1, -1};
    static int[] dy = {+1,-1,  0,  0};
    
    static bool Dijkstra(int x) {
        long INF = 1000000000000000;
        var D = new long[H+2, W+2];
        for(int h=0; h<H+2; ++h) for(int w=0; w<W+2; ++w) D[h,w]=INF;
        D[Sh,Sw]=0;

        var V = new bool[H+2, W+2];
        
        //Console.WriteLine("x:{0}",x);
        while(!V[Gh,Gw]) {
            long Dmin = INF;
            int Dminh=1, Dminw=1;
            for(int h=1; h<=H; ++h)
            for(int w=1; w<=W; ++w)
                if(!V[h,w] && Dmin>D[h,w]) { Dmin=D[h,w]; Dminh=h; Dminw=w; }


            //Console.WriteLine("{0} {1} {2}", Dmin, Dminh, Dminw);
            V[Dminh,Dminw]=true;

            for(int i=0; i<4; ++i) {
                int h = Dminh+dy[i];
                int w = Dminw+dx[i];
                if(V[h,w]) continue;

                if(S[h,w]=='.') D[h,w]=Math.Min(D[h,w], Dmin+1);
                if(S[h,w]=='#') D[h,w]=Math.Min(D[h,w], Dmin+x);
            }
        }
        
        return D[Gh,Gw]<=T;
    }

    static void Main() {
        var buf = Console.ReadLine().Split(new char[]{' '});
        H = int.Parse(buf[0]);
        W = int.Parse(buf[1]);
        T = int.Parse(buf[2]);

        S = new char[H+2,W+2];
        for(int h=0; h<H+2; ++h) { S[h,0]=S[h,W+1]='W'; }
        for(int w=0; w<W+2; ++w) { S[0,w]=S[H+1,w]='W'; }
        
        for(int h=1; h<=H; ++h) {
            string str = Console.ReadLine();
            for(int w=1; w<=W; ++w) {
                S[h,w] = str[w-1];
                if(str[w-1]=='S') { Sh=h; Sw=w; }
                if(str[w-1]=='G') { Gh=h; Gw=w; S[h,w]='.'; }
            }
        }

        int max_ok = 1, min_ng = T;
        while(min_ng-max_ok>1) {
            int tgt = (max_ok+min_ng)/2;
            if(Dijkstra(tgt)) { max_ok = tgt; } else { min_ng = tgt; }
        }

        Console.WriteLine(max_ok);
        
    }


}
