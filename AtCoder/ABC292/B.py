N, Q = map(int, input().split())
C = [0] * N

ans = []

for _ in range(Q):
    t, x = map(int, input().split())

    if t == 1:
        C[x - 1] += 1
    if t == 2:
        C[x - 1] += 2
    if t == 3:
        ans.append("Yes" if C[x - 1] >= 2 else "No")

for a in ans:
    print(a)
