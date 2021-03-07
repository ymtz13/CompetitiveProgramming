using System;
using System.Linq;

class Program
{
  public static void Main()
  {
    var HWNM = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
    int H = HWNM[0], W = HWNM[1], N = HWNM[2], M = HWNM[3];
    var B = new int[H, W];
    var L = new bool[H, W];

    for (int i = 0; i < N; ++i)
    {
      var hw = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
      int h = hw[0] - 1, w = hw[1] - 1;
      B[h, w] = 1;
    }
    for (int i = 0; i < M; ++i)
    {
      var hw = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
      int h = hw[0] - 1, w = hw[1] - 1;
      B[h, w] = 2;
    }

    int ans = 0;
    bool on;
    for (int h = 0; h < H; ++h)
    {
      on = false;
      for (int w = 0; w < W; ++w)
      {
        int b = B[h, w];
        if (b == 1) on = true;
        if (b == 2) on = false;
        if (on && !L[h, w]) { L[h, w] = true; ++ans; }
      }

      on = false;
      for (int w = W - 1; w >= 0; --w)
      {
        int b = B[h, w];
        if (b == 1) on = true;
        if (b == 2) on = false;
        if (on && !L[h, w]) { L[h, w] = true; ++ans; }
      }
    }

    for (int w = 0; w < W; ++w)
    {
      on = false;
      for (int h = 0; h < H; ++h)
      {
        int b = B[h, w];
        if (b == 1) on = true;
        if (b == 2) on = false;
        if (on && !L[h, w]) { L[h, w] = true; ++ans; }
      }

      on = false;
      for (int h = H - 1; h >= 0; --h)
      {
        int b = B[h, w];
        if (b == 1) on = true;
        if (b == 2) on = false;
        if (on && !L[h, w]) { L[h, w] = true; ++ans; }
      }
    }

    Console.WriteLine(ans);
  }

}