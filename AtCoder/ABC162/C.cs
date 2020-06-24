using System;

class Program
{

    static int gcd(int x, int y)
    {
        if(x>y){ int b=x; x=y; y=b; }
        while(x>0) { int b=x; x=y%x; y=b; }
        return y;
    }
    
    static void Main()
    {
        int K = int.Parse(Console.ReadLine())+1;

        int ans = 0;
        for(int i=1; i<K; ++i)
            for(int j=1; j<K; ++j) {
                int x = gcd(i, j);
                for(int k=1; k<K; ++k) ans+=gcd(k, x);
            }

        
        Console.WriteLine(ans);    

    }

    

}
