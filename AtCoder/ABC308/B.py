N, M = map(int, input().split())
C = list(input().split())
D = list(input().split())
P = list(map(int, input().split()))
P0 = P[0]

M = {}
for d, p in zip(D, P[1:]):
    M[d] = p

ans = 0
for c in C:
    if c in M:
        ans += M[c]
    else:
        ans += P0

print(ans)
