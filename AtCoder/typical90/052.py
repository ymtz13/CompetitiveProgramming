N = int(input())
ans = 1
mod = 10**9 + 7
for _ in range(N):
  S = sum(map(int, input().split()))
  ans *= S
  ans %= mod

print(ans)
