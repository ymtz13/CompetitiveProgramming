mod = 998244353

N, M, K = map(int, input().split())
W = [int(input()) for _ in range(N)]

if N == 1:
  print(1)
  exit()

Nh = N // 2


def f(W):
  D = [[0] * len(W) for _ in range(K + 1)]

  return D


D1 = f(W[:Nh])
D2 = f(W[Nh:])
