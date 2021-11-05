N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

m = min(T)
for i, t in enumerate(T):
  if t == m: break

t = 10**10
ans = [None] * N
for i in range(i, i + N):
  i %= N

  t = min(t + S[(i - 1) % N], T[i])
  ans[i] = t

for a in ans:
  print(a)
