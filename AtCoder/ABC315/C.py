N = int(input())
FS = [tuple(map(int, input().split())) for _ in range(N)]

M = [[] for _ in range(N + 10)]

for f, s in FS:
    M[f].append(s)

ans = 0
Z = []
for m in M:
    m.sort(reverse=True)
    if m:
        Z.append(m[0])
    if len(m) >= 2:
        ans = max(ans, m[0] + m[1] // 2)

Z.sort(reverse=True)
ans = max(ans, sum(Z[:2]))

print(ans)
