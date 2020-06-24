N, M = map(int, input().split())
E = [[] for _ in range(N)]

for _ in range(M):
    A, B = map(int, input().split())
    E[A-1].append(B-1)
    E[B-1].append(A-1)

ans = [None]*N
ans[0]=-1

queue=[0]
while queue:
    queue_new = []
    for q in queue:
        for e in E[q]:
            if ans[e] is not None: continue
            ans[e]=q
            queue_new.append(e)

    queue = queue_new

print("Yes")
for a in ans[1:]:
    print(a+1)
