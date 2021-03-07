using System;

// 2345
// [0-1][000-999]
// 2[0-2][00-99]
// 23[0-3][0-9]
// 234[0-4]
// 2345

class Program
{
    static long[] ALL, OK;
    static long[] P = {0, 1, 2, 3, 4, 4, 5, 6, 7, 8};
    
    static long F(long S)
    {
        long retval = S;
        bool ok = true;
        for(int i=19; i>=0 && ok; --i) {
            long X = S / ALL[i];
            S -= X*ALL[i];
            retval -= OK[i]*P[X];
            if(X==4 || X==9) ok = false;
        }
        if (ok) --retval;
        return retval;
    }
    
    public static void Main()
    {
        ALL = new long[20];
        OK  = new long[20];
        long all = 1, ok = 1;
        for(int i=0; i<20; ++i) {
            ALL[i] = all;
            OK[i] = ok;
            all *= 10;
            ok *= 8;
        }
        
        var AB = Console.ReadLine().Split(' ');
        long A = long.Parse(AB[0]), B = long.Parse(AB[1]);
        Console.WriteLine(F(B)-F(A-1));
    }
}
