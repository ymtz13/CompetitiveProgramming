N, K = map(int, input().split())
S = [int(input()) for _ in range(N)]

if 0 in S:
    print(N)
    exit()

p = 1
l = -1
ans = 0
for r in range(N):
    p *= S[r]
    while p>K and l<r:
        l += 1
        p //= S[l]
    ans = max(ans, r-l)

print(ans)
