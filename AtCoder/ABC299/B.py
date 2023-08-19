N, T = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))

c1 = C[0]
rTmax = -1
iTmax = None
r1max = 0
i1max = None
for i, (c, r) in enumerate(zip(C, R)):
    if c == T:
        if r > rTmax:
            rTmax = r
            iTmax = i + 1

    if c == c1:
        if r > r1max:
            r1max = r
            i1max = i + 1

print(iTmax if rTmax > -1 else i1max)
