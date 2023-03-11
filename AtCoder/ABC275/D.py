from sys import setrecursionlimit

setrecursionlimit(1000000)

N = int(input())

memo = {}


def f(N):
  if N in memo: return memo[N]
  if N == 0: return 1

  retval = f(N // 2) + f(N // 3)
  memo[N] = retval

  return retval


print(f(N))
