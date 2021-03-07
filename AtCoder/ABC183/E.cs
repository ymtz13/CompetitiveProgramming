using System;
using System.Linq;

class Program
{
  public static void Main()
  {
    var HW = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
    int H = HW[0], W = HW[1];
    long mod = 1000000007;

    var S = new bool[H + 2, W + 2];
    for (int h = 1; h <= H; ++h)
    {
      var s = Console.ReadLine();
      for (int w = 1; w <= W; ++w)
      {
        S[h, w] = s[w - 1] == '.';
      }
    }

    var X = new long[H + 2, W + 2];
    var Z = new long[H + 2, W + 2, 3];
    X[1, 1] = 1;
    Z[1, 1, 0] = Z[1, 1, 1] = Z[1, 1, 2] = 1;

    for (int h = 1; h <= H; ++h)
    {
      for (int w = 1; w <= W; ++w)
      {
        if (!S[h, w]) continue;
        if (h == 1 && w == 1) continue;

        X[h, w] = (Z[h, w - 1, 0] + Z[h - 1, w, 1] + Z[h - 1, w - 1, 2]) % mod;
        Z[h, w, 0] = (Z[h, w - 1, 0] + X[h, w]) % mod;
        Z[h, w, 1] = (Z[h - 1, w, 1] + X[h, w]) % mod;
        Z[h, w, 2] = (Z[h - 1, w - 1, 2] + X[h, w]) % mod;
      }
    }

    Console.WriteLine(X[H, W]);
  }

}