from bisect import bisect

INF = 1 << 70

N, T, Q = map(int, input().split())

AD = []
AD += [(-INF, 1)]
AD += [tuple(map(int, input().split())) for _ in range(N)]
AD += [(+INF, 2)]


R = []
prev = AD[0]
for a, d in AD[1:]:
    pa, pd = prev
    prev = (a, d)

    if pd == 1 and d == 2:
        R.append((pa + a) // 2)


ans = []
for _ in range(Q):
    X = int(input())
    a, d = AD[X]
    i = bisect(R, a)

    if d == 2:
        i -= 1
    r = R[i]

    if d == 1:
        ans.append(min(r, a + T))
    else:
        ans.append(max(r, a - T))


for a in ans:
    print(a)
