using System;

class Program
{
    static void Main()
    {
        var N = int.Parse(Console.ReadLine());

        var T = new int[24*12+1];
        for(int i=0; i<N; ++i) {
            var str = Console.ReadLine().Split(new char[] {'-'});
            int s = int.Parse(str[0]);
            s -= s%5;
            int sh = s/100, sm = s%100;
            T[sh*12+sm/5]++;

            int e = int.Parse(str[1]);
            if(e%5>0) e += 5-e%5;
            int eh = e/100, em = e%100;
            T[eh*12+em/5]--;

        }

        int r=0;
        for(int t=0; t<24*12+1; ++t) {
            int h=t/12, m=(t%12)*5;
            //Console.WriteLine("{0}:{1} -> {2}",h,m,T[t]);
            if(T[t]>0) {
                if(r==0) { Console.Write("{0:00}{1:00}-", h, m); }
                r += T[t];
            }
            if(T[t]<0) {
                r += T[t];
                if(r==0) { Console.WriteLine("{0:00}{1:00}", h, m); }
            }


        }


    }

}
