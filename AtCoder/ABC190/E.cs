using System;
using System.Collections.Generic;
using System.Linq;

class Program 
{
  static public void Main()
  {
    var NM = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
    int N = NM[0], M = NM[1];

    var E = new List<int>[N];
    for(int i=0; i<N; ++i) E[i] = new List<int>();
    for (int i=0; i<M; ++i) {
      var AB = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
      int A = AB[0], B = AB[1];
      E[A-1].Add(B-1);
      E[B-1].Add(A-1);
    }

    for(int i=0; i<N; ++i) {
      for(int c=0; c<E[i].Count; ++c) Console.Write(E[i][c]);
      Console.WriteLine();
    }

    

  }
}