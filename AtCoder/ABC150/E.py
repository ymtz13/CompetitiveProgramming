N = int(input())
C = sorted(list(map(int, input().split())), reverse=True)

ans = 0
mod = 10**9+7
for r, c in enumerate(C):
    ans += c*(r+2)

ans = ans * 2**(2*N-2) % mod
print(ans)

