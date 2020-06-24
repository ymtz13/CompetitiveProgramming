using System;
using System.Numerics;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        string[] buf;
        buf = Console.ReadLine().Split(new char[]{' '});
        int N = int.Parse(buf[0]);
        int a = int.Parse(buf[1]);

        //var k = BigInteger.Parse(Console.ReadLine());
        var k = Console.ReadLine();

        //Console.WriteLine(k);

        buf = Console.ReadLine().Split(new char[]{' '});
        int[] B = new int[N];
        for(int i=0; i<N; ++i) B[i] = int.Parse(buf[i]);

        var T = new int[N];
        var L = new int[N];
        int j = 1;
        int kf = k.Length<10 ? int.Parse(k) : 100000000;
        while(T[a-1]==0 && j<=kf){
            T[a-1] = j++;
            a = L[j-2] = B[a-1];
        }

        if(j==kf+1) {
            Console.WriteLine(a);
        } else {
            int loop = j-T[a-1];
            int tail = T[a-1];
            //int k_ = tail + (int)((k-tail)%loop);
            long k_ = 0;
            foreach(var c in k) {
                k_ = (k_*10+(c-'0'))%loop;
            }
            k_ = (k_-tail+loop*1000000)%loop;
            k_ += tail;
            //Console.WriteLine("L : " + string.Join(" ", L));
            //Console.WriteLine($"{loop} {tail} {k_}");
            Console.WriteLine(L[k_-1]);
        }

    }

}
