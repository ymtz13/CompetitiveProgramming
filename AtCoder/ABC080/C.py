
N = int(input())
F = []
for _ in range(N):
    F.append(sum([int(f)<<i for i, f in enumerate(input().split())]))

P = [list(map(int, input().split())) for _ in range(N)]
B = []
for d in range(1,1024):
    b = 0
    for f, p in zip(F,P):
        c = 0
        ovlp = d&f
        while ovlp:
            if ovlp&1: c+=1
            ovlp>>=1
        b+=p[c]
    B.append(b)

print(max(B))

