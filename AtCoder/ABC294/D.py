from heapq import heappop, heappush

N, Q = map(int, input().split())

q1 = list(range(1, N + 1))
q2 = []
D = [False] * (N + 1)
ans = []

for _ in range(Q):
    ev = input().split()
    t = int(ev[0])

    if t == 1:
        heappush(q2, heappop(q1))

    if t == 2:
        x = int(ev[1])
        D[x] = True

    if t == 3:
        while True:
            x = heappop(q2)
            if not D[x]:
                heappush(q2, x)
                break

        ans.append(x)

for a in ans:
    print(a)
