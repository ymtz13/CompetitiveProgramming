N, M = map(int, input().split())
V = [0] * (N + 1)
A = [(i + 1, int(input())) for i in range(N)]

for _ in range(M):
    B = int(input())
    for i, a in A:
        if a <= B:
            V[i] += 1
            break

m = max(V)
for i, v in enumerate(V):
    if v == m:
        print(i)
