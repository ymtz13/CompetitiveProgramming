N, M = map(int, input().split())
H = list(map(int, input().split()))

E = [[] for _ in range(N)]
for m in range(M):
    A, B = map(int, input().split())
    E[A-1].append(B-1)
    E[B-1].append(A-1)

ans = 0
for i in range(N):
    good = True
    for j in E[i]:
        if H[i]<=H[j]:
            good=False
            break
    if good: ans+=1

print(ans)
