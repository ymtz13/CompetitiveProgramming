from heapq import heappop, heappush
from collections import defaultdict

N, K, Q = map(int, input().split())
ans = []

h1 = [0] * K
d1 = defaultdict(int)
d1[0] = K
s1 = 0
c1 = K

h2 = [0] * (N - K)
d2 = defaultdict(int)
d2[0] = N - K
c2 = N - K

A = [0] * N

for _ in range(Q):
    X, Y = map(int, input().split())
    removed = A[X - 1]
    added = Y
    A[X - 1] = Y

    if removed >= h1[0]:
        d1[removed] -= 1
        s1 -= removed
        while h1 and d1[h1[0]] == 0:
            heappop(h1)

        heappush(h2, -added)
        d2[added] += 1

        while True:
            moved = -heappop(h2)
            if d2[moved] > 0:
                break
        d2[moved] -= 1
        while h2 and d2[-h2[0]] == 0:
            heappop(h2)

        heappush(h1, moved)
        d1[moved] += 1
        s1 += moved

    else:
        d2[removed] -= 1

        heappush(h2, -added)
        d2[added] += 1
        while h2 and d2[-h2[0]] == 0:
            heappop(h2)

        if h1[0] < -h2[0]:
            moved = -heappop(h2)
            d2[moved] -= 1
            while h2 and d2[-h2[0]] == 0:
                heappop(h2)
            heappush(h1, moved)
            d1[moved] += 1
            s1 += moved

            moved = heappop(h1)
            d1[moved] -= 1
            s1 -= moved
            while h1 and d1[h1[0]] == 0:
                heappop(h1)
            heappush(h2, -moved)
            d2[moved] += 1

    # print(h1)
    # print(d1)
    # print(s1)
    # print(h2)
    # print(d2)
    # print()

    ans.append(s1)


for a in ans:
    print(a)
