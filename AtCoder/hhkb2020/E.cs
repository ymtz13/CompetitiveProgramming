using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static int H, W;
    static long K;
    static string[] S;
    static long[,] M;

    static long Power(long x, long k, long mod) {
        long retval = 1;
        for(; k>0; k>>=1) {
            if((k&1)==1) retval = retval * x % mod;
            x = x * x % mod;
        }
        return retval;
    }    
    
    public static void Main()
    {
        var HW = Console.ReadLine().Split(' ').Select(int.Parse).ToList();
        H = HW[0]; W = HW[1];

        S = new string[H];
        for(int h=0; h<H; ++h) S[h] = Console.ReadLine();

        for(int h=0; h<H; ++h) {
            for(int w=0; w<W; ++w) {
                if(S[h][w]=='.') ++K;
            }
        }
        
        M = new long[H, W];

        // Right
        for(int h=0; h<H; ++h) {
            int r = 0;
            for(int w=0; w<W; ++w) {
                r = S[h][w]=='.' ? r+1 : 0;
                M[h,w] += r;
            }
        }
        
        // Left
        for(int h=0; h<H; ++h) {
            int r = 0;
            for(int w=W-1; w>=0; --w) {
                r = S[h][w]=='.' ? r+1 : 0;
                M[h,w] += r;
            }
        }

        // Down
        for(int w=0; w<W; ++w) {
            int r = 0;
            for(int h=0; h<H; ++h) {
                r = S[h][w]=='.' ? r+1 : 0;
                M[h,w] += r;
            }
        }

        // Up
        for(int w=0; w<W; ++w) {
            int r = 0;
            for(int h=H-1; h>=0; --h) {
                r = S[h][w]=='.' ? r+1 : 0;
                M[h,w] += r;
            }
        }


        long ans = 0;
        long mod = 1000000007;
        long A = Power(2, K, mod);
        for(int h=0; h<H; ++h) {
            for(int w=0; w<W; ++w) {
                if(S[h][w]=='#') continue;
                long m = M[h,w]-3;
                long x = (A - Power(2, K-m, mod) + mod) % mod;
                ans = (ans + x) % mod;
            }
        }
        
        Console.WriteLine(ans);
    }

}
