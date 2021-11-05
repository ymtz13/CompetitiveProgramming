N = int(input())
A = list(map(int, input().split()))
S = M = T = 0
for i, a in enumerate(A):
  S += a
  T += S
  M = max(M, a)
  print(T + M*(i+1))
