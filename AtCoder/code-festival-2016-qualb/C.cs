using System;
using System.Collections.Generic;

struct Item
{
    public Item(long cost, long dir) {
        Cost = cost;
        Dir = dir;
    }

    public long Cost { get; }
    public long Dir { get; }
}

class Program
{
    public static void Main()
    {
        var str = Console.ReadLine().Split(' ');
        long W = long.Parse(str[0]), H = long.Parse(str[1]);

        var L = new List<Item>();
        for(int i=0; i<W; ++i) L.Add(new Item(long.Parse(Console.ReadLine()), 0));
        for(int i=0; i<H; ++i) L.Add(new Item(long.Parse(Console.ReadLine()), 1));
        L.Sort(delegate(Item x, Item y){ return (int)y.Cost - (int)x.Cost; });

        long ans = 0;
        var N = new long[2];
        for(int i=0; i<W+H; ++i) {
            var x = L[i];
            ans += (N[1-x.Dir] + 1) * x.Cost;
            ++N[x.Dir];
        }

        Console.WriteLine(ans);
    }
}
