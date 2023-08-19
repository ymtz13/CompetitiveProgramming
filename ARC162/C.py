from collections import deque

T = int(input())
ans = []

for _ in range(T):
    N, K = map(int, input().split())
    P = [None] + [p - 1 for p in map(int, input().split())]
    A = list(map(int, input().split()))

    C = [[] for _ in range(N)]
    for i, p in enumerate(P[1:], 1):
        C[p].append(i)

    order = []
    queue = deque([0])
    while queue:
        q = queue.popleft()
        order.append(q)
        for c in C[q]:
            queue.append(c)

    S = [None] * N
    Empty = [0] * N
    Dead = [None] * N
    a = False
    for q in reversed(order):
        s = set()
        if A[q] != -1 and A[q] < K:
            s.add(A[q])

        empty = 1 if A[q] == -1 else 0
        dead = A[q] == K

        for c in C[q]:
            s |= S[c]
            empty += Empty[c]
            dead = dead or Dead[c]

        S[q] = s
        Empty[q] = empty
        Dead[q] = dead

        if len(s) == K and empty <= 1 and not dead:
            a = True
        if len(s) == K - 1 and empty == 1 and not dead:
            a = True

    ans.append(a)

    # print(S)
    # print(Empty)
    # print(Dead)

for a in ans:
    print("Alice" if a else "Bob")
