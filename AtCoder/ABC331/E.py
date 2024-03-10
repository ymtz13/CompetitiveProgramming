from heapq import heappush, heappop

N, M, L = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

K = max(N, M) + 5
K2 = K * K

INF = 10**20

A = [v * K2 + i * K for i, v in enumerate(A)]
B = [v * K2 + i for i, v in enumerate(B)] + [-INF]

A0 = A[:]

A.sort(reverse=True)
B.sort(reverse=True)

S = set()
for _ in range(L):
    c, d = map(int, input().split())
    S.add((c - 1) * K + (d - 1))

b0 = B[0]

Z = [1] * K
heap = []
for a in A:
    heappush(heap, -(a + b0))

while True:
    v = -heappop(heap)

    price = v // K2
    ij = v % K2
    i = ij // K
    j = ij % K

    if ij not in S:
        print(price)
        exit()

    b = B[Z[i]]
    Z[i] += 1
    heappush(heap, -(A0[i] + b))
