N, S, K = map(int, input().split())
ans = 0
for _ in range(N):
    P, Q = map(int, input().split())
    ans += P * Q

if ans < S:
    ans += K

print(ans)
