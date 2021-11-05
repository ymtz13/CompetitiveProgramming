N = int(input())
A = sorted(list(map(int, input().split())))
p = 0
D = []
for a in A:
  D.append(a-p)
  p = a

ans = 1
mod = 10**9+7
for d in D:
  ans = ans * (d+1) % mod

print(ans)
