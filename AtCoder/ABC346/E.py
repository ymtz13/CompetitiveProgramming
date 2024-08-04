H, W, M = map(int, input().split())
Queries = [tuple(map(int, input().split())) for _ in range(M)]

nH = H
nW = W

sRow = set()
sCol = set()

ans = [0] * 200010
for T, A, X in reversed(Queries):
    if T == 1:
        if A in sRow:
            continue
        sRow.add(A)
        nH -= 1
        ans[X] += nW
    else:
        if A in sCol:
            continue
        sCol.add(A)
        nW -= 1
        ans[X] += nH

suma = sum(ans)
ans[0] += H * W - suma

K = len([a for a in ans if a > 0])
print(K)
for x, a in enumerate(ans):
    if a > 0:
        print(x, a)
