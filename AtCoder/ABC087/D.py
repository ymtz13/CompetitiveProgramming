N, M = list(map(int, input().split()))

edges = [[] for _ in range(N+1)]
for _ in range(M):
    L, R, D = list(map(int, input().split()))
    edges[L].append((R, D))
    edges[R].append((L,-D))

x = [None]*(N+1)
for i in range(1,N+1):
    if x[i] is not None: continue
    queue = [i]
    x[i] = 0
    minx = maxx = 0
    while len(queue)>0:
        queue_new = []
        for q in queue:
            for r, d in edges[q]:
                dist = x[q] + d
                print('from view of', q, r, 'should be at', dist)
                if x[r]==None:
                    x[r] = dist
                    queue_new.append(r)
                elif x[r]!=dist:
                    print('No')
                    exit()
                    
        queue = queue_new

print(x)
print('Yes')
