from heapq import heappush, heappop

N, M = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
    U, V, W = map(int, input().split())
    U -= 1
    V -= 1
    E[U].append((V, W))
    E[V].append((U, W))

K = int(input())
A = [i - 1 for i in map(int, input().split())]

D = int(input())
X = list(map(int, input().split()))

infected = [-1] * N
for a in A:
    infected[a] = 0

newInfected = A[:]
heap = []

for day, x in enumerate(X, 1):
    for i in newInfected:
        heappush(heap, i)

    newInfectedNext = set()

    while heap:
        v = heappop(heap)
        d = v // N
        q = v % N
        # print(q + 1, d, x)
        if d > x:
            heappush(heap, v)
            break
        if q in newInfectedNext:
            continue
        if infected[q] == -1:
            newInfectedNext.add(q)

        for e, dd in E[q]:
            if infected[e] == -1:
                heappush(heap, (d + dd) * N + e)

    # print(day, infected, newInfected, newInfectedNext)

    for i in newInfectedNext:
        infected[i] = day

    newInfected = list(newInfectedNext)

for day in infected:
    print(day)
