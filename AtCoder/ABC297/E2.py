from heapq import heappop, heappush

N, K = map(int, input().split())
A = set(map(int, input().split()))

A = sorted(list(A))
a0 = A[0]

heap = []
base = {0}
for k in range(1, K + 1):
    x = k * a0
    heappush(heap, -x)
    base.add(x)


for a in A[1:]:
    for b in set(base):
        for k in range(1, K + 1):
            x = b + k * a
            if x in base:
                break
            if x >= -heap[0]:
                break
            # print("added", x)
            base.add(x)
            heappop(heap)
            heappush(heap, -x)

print(-heap[0])
