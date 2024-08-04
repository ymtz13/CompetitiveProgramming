from heapq import heappop, heappush

N, K = map(int, input().split())
P = [p - 1 for p in list(map(int, input().split()))]
L = [0] * N
for i, p in enumerate(P):
    L[p] = i

ans = []
for d in range(N):
    while True:
        con = False
        for s in range(N - d):
            t = s + d
            ls = L[s]
            lt = L[t]

            if lt + K <= ls:
                ans.append((lt + 1, ls + 1))
                con = True
                L[s] = lt
                L[t] = ls

        if not con:
            break

print(len(ans))
for s, t in ans:
    print(s, t)
