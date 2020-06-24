using System;
using System.Collections.Generic;

class Point{
    public int x,y;
    public Point(int x, int y) {this.x=x; this.y=y;}
}

class Program
{
    static void Main()
    {
        string[] buf;
        buf = Console.ReadLine().Split(" ");
        var N = int.Parse(buf[0]);
        var X = int.Parse(buf[1]);
        var Y = int.Parse(buf[2]);

        var offset = 202;
        var dist = new int[405, 405];
        for(int i=0; i<405; ++i) {
            dist[  0, i] = -1;
            dist[404, i] = -1;
            dist[i,   0] = -1;
            dist[i, 404] = -1;
        }
        
        for(int i=0; i<N; ++i) {
            buf = Console.ReadLine().Split(" ");
            var x = int.Parse(buf[0]);
            var y = int.Parse(buf[1]);
            dist[x+offset, y+offset] = -1;
        }

        var queue = new List<Point>(){ new Point(offset,offset) };
        var darray = new List<int>(){ 0 };
        int iq = 0;
        while(iq<queue.Count) {
            var p = queue[iq];
            var d = darray[iq];
            iq++;

            int x = p.x, y = p.y;
            //Console.WriteLine("{0},{1} ->{2}", x-offset, y-offset, d);

            if(dist[x,y]!=0) continue;
            
            dist[x,y] = d;
            if(dist[x+1,y+1]==0){ queue.Add(new Point(x+1,y+1)); darray.Add(d+1); }
            if(dist[x  ,y+1]==0){ queue.Add(new Point(x  ,y+1)); darray.Add(d+1); }
            if(dist[x-1,y+1]==0){ queue.Add(new Point(x-1,y+1)); darray.Add(d+1); }
            if(dist[x+1,y  ]==0){ queue.Add(new Point(x+1,y  )); darray.Add(d+1); }
            if(dist[x-1,y  ]==0){ queue.Add(new Point(x-1,y  )); darray.Add(d+1); }
            if(dist[x  ,y-1]==0){ queue.Add(new Point(x  ,y-1)); darray.Add(d+1); }
            
        }

        var ans = dist[X+offset, Y+offset];
        Console.WriteLine(ans==0 ? -1 : ans);

    }

}
