using System;
using System.Linq;

class Program
{
  static void Main()
  {
    var ABC = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
    int A = ABC[0], B = ABC[1], C = ABC[2];
    var N = A + B + C;

    var dp = new double[101, 101, 101];

    dp[A, B, C] = 1;

    for (int a = A; a < 100; ++a)
    {
      for (int b = B; b < 100; ++b)
      {
        for (int c = C; c < 100; ++c)
        {
          if (a == A && b == B && c == C) continue;

          var n = a + b + c - 1;
          var pa = a > 0 ? dp[a - 1, b, c] * (double)(a - 1) / n : 0;
          var pb = b > 0 ? dp[a, b - 1, c] * (double)(b - 1) / n : 0;
          var pc = c > 0 ? dp[a, b, c - 1] * (double)(c - 1) / n : 0;
          dp[a, b, c] = pa + pb + pc;
        }
      }
    }

    double ans = 0;

    for (int x = 0; x < 100; ++x)
    {
      for (int y = 0; y < 100; ++y)
      {
        var n = 99 + x + y;
        var t = 100 + x + y - N;
        var pa = dp[99, x, y] * (99.0 / n);
        var pb = dp[y, 99, x] * (99.0 / n);
        var pc = dp[x, y, 99] * (99.0 / n);
        ans += t * (pa + pb + pc);
      }
    }

    Console.WriteLine(ans);


  }

}