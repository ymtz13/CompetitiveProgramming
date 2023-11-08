from collections import deque

N, M =map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

E = [[] for _ in range(N)]

for a, b in zip(A, B):
    E[a-1].append(b-1)
    E[b-1].append(a-1)

dist = [-1]*N
for st in range(N):
    if dist[st]!=-1:
        continue
    queue = deque([st*2])
    while queue:
        q = queue.popleft()
        i, d = q//2, q%2
        if dist[i] ==d: continue

        if dist[i] != -1:
            print('No')
            exit()
        dist[i] = d

        for e in E[i]:
            queue.append(e*2+1-d)

print('Yes')
