N, Q = map(int, input().split())
S = input()
Queries = [tuple(map(int, input().split())) for _ in range(Q)]

A = [0]
for cL, c in zip(S, S[1:]):
    A.append(A[-1])
    if cL == c:
        A[-1] += 1

for L, R in Queries:
    print(A[R - 1] - A[L - 1])
