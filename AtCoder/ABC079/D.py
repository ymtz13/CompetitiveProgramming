H, W = list(map(int, input().split()))
C = [list(map(int, input().split())) for _ in range(10)]
P = [c[:] for c in C]

for k in range(10):
    for i in range(10):
        for j in range(10):
            P[i][j] = min(P[i][j], P[i][k]+P[k][j])

ans = 0
for _ in range(H):
    for a in map(int, input().split()):
        if a!=-1:
            ans += P[a][1]
    
print(ans)
