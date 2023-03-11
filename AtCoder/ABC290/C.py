N, K = map(int, input().split())
A = list(map(int, input().split()))
S = set(A)

mex = 0
while mex in S:
  mex += 1

print(min(mex, K))
