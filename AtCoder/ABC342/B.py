N = int(input())
P = list(map(int, input().split()))
O = [None] * (N + 1)
for i, p in enumerate(P):
    O[p] = i
Q = int(input())
Queries = [tuple(map(int, input().split())) for _ in range(Q)]
for A, B in Queries:
    print(A if O[A] < O[B] else B)
