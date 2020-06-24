N = int(input())

E = []

for n in range(N):
    A = int(input())
    for _ in range(A):
        x, y = list(map(int, input().split()))
        E.append((n, x-1, y))

ans = 0
for k in range((1<<N)-1, -1, -1):
    l = [(k>>i)&1 for i in range(N)]
    OK = True
    for e0, e1, e2 in E:
        if (l[e0]==1 and l[e1]!=e2):
            OK = False
            break
    if OK: ans = max(ans, sum(l))

print(ans)
