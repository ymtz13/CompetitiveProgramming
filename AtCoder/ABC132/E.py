N, M = [int(c) for c in input().split()]
path = [[] for _ in range(N)]
for i in range(M):
    u, v = [int(c) for c in input().split()]
    path[u-1].append(v-1)

S, T = [int(c)-1 for c in input().split()]

reach = [[-1 for _ in range(N)] for _ in range(3)]
reach[0][S] = 0

queue={S}

time = 1
for _ in range(4*N):
    queue_new = set()
    for q in queue:
        for v in path[q]:
            if reach[time%3][v]==-1:
                reach[time%3][v]=time
                queue_new.add(v)

    queue = queue_new
    time += 1

if reach[0][T]==-1:
    print(-1)
else:
    print(reach[0][T]//3)
    
