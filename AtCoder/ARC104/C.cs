using System;

class Program
{
    static int PairR  = 1000;
    static int PairL  = 2000;
    static int NoData = 3000;

    static int[] P;
    static int[] Q;
    
    static bool Check(int j, int i)
    {
        int L = i-j;
        var result = true;

        for(int k=j*2; k<j*2+L; ++k) {
            int p = k+L;

            //Console.WriteLine($"{k},{p},{P[k]}, {P[p]}");

            if(P[k]==PairR) {
                if(P[p]!=NoData) { result = false; break; }
            }
            else if (P[k]==PairL) { result = false; break; }
            else if (P[k]==NoData) {}
            else {
                if(P[k]!=p) { result = false; break; }
                if(P[p]!=k || Q[k]!=Q[p]) { result = false; break; }
            }
            
        }
        for(int k=j*2+L; k<i*2; ++k) {
            int p = k-L;

            if(P[k]==PairL) {
                if(P[p]!=NoData) { result = false; break; }
            }
            else if (P[k]==PairR) { result = false; break; }
            else if (P[k]==NoData) {}
            else {
                if(P[k]!=p) { result = false; break; }
                if(P[p]!=k || Q[k]!=Q[p]) { result = false; break; }
            }
            
        }

        return result;
    }
    
    static void Main()
    {
        int N = int.Parse(Console.ReadLine()), N2 = N*2;
        P = new int[N2];
        Q = new int[N2];
        for(int i=0; i<N2; ++i) P[i] = NoData;

        var E = new bool[N2];
        var No = false;
        
        string[] str;
        for(int i=1; i<=N; ++i) {
            str = Console.ReadLine().Split(' ');
            int A = int.Parse(str[0]), B = int.Parse(str[1]);
            if(A!=-1 && B!=-1){ P[A-1] = B-1; P[B-1] = A-1; }
            else if(A!=-1) { P[A-1] = PairR; }
            else if(B!=-1) { P[B-1] = PairL; }

            if(A!=-1) {
                Q[A-1] = i;
                No |= E[A-1];
                E[A-1] = true;
            }

            if(B!=-1) {
                Q[B-1] = i;
                No |= E[B-1];
                E[B-1] = true;
            }
        }

        if(No){Console.WriteLine("No"); return;}
        
        var dp = new bool[N+1];
        dp[0] = true;

        //Console.WriteLine($"{Check(0,2)}");        

        for(int i=1; i<=N; ++i) {
            var result = false;
            for(int j=i-1; j>=0 && !result; --j) {
                //Console.WriteLine($"i: {i}, dp[{j}]: {dp[j]}");
                if(!dp[j]) continue;
                result = Check(j, i);
            }
            dp[i] = result;
        }

        
        Console.WriteLine(dp[N] ? "Yes" : "No");
    }
}
