import heapq

N = int(input())
T = [list(map(int, input().split()))[1:] + [-1, -1] for _ in range(N)]
exist = [[True]*len(t) for t in T]

h1 = []
h2 = []
for i, t in enumerate(T):
    heapq.heappush(h1, (-t[0], i, 0))
    heapq.heappush(h2, (-t[0], i, 0))
    heapq.heappush(h2, (-t[1], i, 1))

Item1 = [0]*N
Item2 = [1]*N
    
M = int(input())
A = map(int, input().split())
for a in A:
    h = h1 if a==1 else h2
    
    while True:
        t, i, j = heapq.heappop(h)
        if exist[i][j]: break
    print(-t)
    exist[i][j] = False

    if j==Item1[i]:
        item2 = Item2[i]
        heapq.heappush(h1, (-T[i][item2  ], i, item2  ))
        heapq.heappush(h2, (-T[i][item2+1], i, item2+1))
        Item1[i] = item2
        Item2[i] += 1

    else:
        item2 = Item2[i]
        heapq.heappush(h2, (-T[i][item2+1], i, item2+1))
        Item2[i] += 1
        
