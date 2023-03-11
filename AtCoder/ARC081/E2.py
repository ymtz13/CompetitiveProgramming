from string import ascii_lowercase
from sys import setrecursionlimit

setrecursionlimit(1 << 20)

ascii_lowercase = 'abc'
nchar = len(ascii_lowercase)

A = input()
N = len(A)

S = set()
K = [N]
for i in range(N - 1, -1, -1):
  a = A[i]
  S.add(a)
  if len(S) == nchar:
    K.append(i)
    S = set()

K = K[::-1]

ans = []


def solve(A, K, x):
  k = K[0]
  if k == x:
    ans.append('a' * len(K))
    return

  print(A, K, x)
  s = {a for a in A[x:k]}
  for c in ascii_lowercase:
    if c not in s: break

  ans.append(c)
  if len(K) == 1: return

  for i in range(k, K[1]):
    if A[i] == c: break

  solve(A, K[1:], i + 1)


solve(A, K, 0)

print(''.join(ans))
