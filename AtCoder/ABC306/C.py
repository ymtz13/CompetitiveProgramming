N = int(input())
A = list(map(int, input().split()))
I = [[] for _ in range(N + 1)]
for i, a in enumerate(A):
    I[a].append(i)

J = []
for a in range(1, N + 1):
    J.append((I[a][1], a))

J.sort()

print(*[a for _, a in J])
