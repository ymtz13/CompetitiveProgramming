mod = 10**9 + 7
N = int(input())
X = list(map(int, input().split()))

n = 0
ans = 1
for x in X:
  n += 1
  if n > (x + 1) // 2:
    ans = ans * n % mod
    n -= 1

for i in range(1, n+1):
  ans = ans * i % mod

print(ans)
