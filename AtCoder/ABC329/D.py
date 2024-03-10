from heapq import heappush

N, M = map(int, input().split())
A = list(map(int, input().split()))

C = [0] * N

heap = []

ans = []
for a in A:
    a -= 1

    C[a] += 1
    heappush(heap, -C[a] * N + a)

    i = heap[0] % N
    ans.append(i + 1)

for a in ans:
    print(a)
