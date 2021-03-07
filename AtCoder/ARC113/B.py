A, B, C = map(int, input().split())

M = [1]*10
T = list(range(10))
while B:
  if B&1:
    M = [m*t%10 for m, t in zip(M, T)]
  T = [t*t%10 for t in T]
  B>>=1

#print(T)
#print(M)

A %= 10
while C:
  if C&1:
    A = M[A]
  M = [M[m] for m in M]
  C >>= 1

print(A)
