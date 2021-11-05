N = int(input())
C = sorted(list(map(int, input().split())))
mod = 10**9+7

ans = 1
for i, c in enumerate(C):
  ans = ans*max(c-i, 0)%mod

print(ans)
