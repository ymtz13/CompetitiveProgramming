using System;
using System.Collections.Generic;

class Program
{

    static void Main()
    {
        int N = int.Parse(Console.ReadLine());
        string s = Console.ReadLine();
        int[] S = new int[N];

        var D = new Dictionary<char, int>() {{'R', 0}, {'G', 1}, {'B', 2}};
        for(int i=0; i<N; ++i) S[i]=D[s[i]];

        int[,] X = new int[3,N];
        int[] nC = new int[] {0, 0, 0};
        for(int i=N-1; i>=0; --i) {
            for(int j=0; j<3; ++j) X[j, i] = nC[j];
            ++nC[S[i]];
        }

        long ans=0;
        for(int i=0; i<N-2; ++i) {
            for(int j=i+1; j<N-1; ++j) {
                if(S[i]==S[j]) continue;
                
                int r = 3-S[i]-S[j];
                ans += X[r, j];
                
                int k = 2*j-i;
                if (k<N && S[k]==r) --ans;
            }
        }

        Console.WriteLine(ans);

    }

}
