from heapq import heappop, heappush

N, M = map(int, input().split())
A = list(map(int, input().split()))

C = [0] * (M + 1)
for a in A:
    C[a] += 1

heap = []

ans = []
S = set()

last = -1
for i, a in enumerate(A):
    C[a] -= 1
    heappush(heap, (a, i))

    if C[a] == 0 and a not in S:
        while True:
            aa, j = heappop(heap)
            if aa not in S and last < j:
                ans.append(aa)
                S.add(aa)
                last = j

                if aa == a:
                    break

print(*ans)
