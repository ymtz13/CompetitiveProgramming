N = int(input())

A = []
for _ in range(N):
    C = int(input())
    A.append(list(map(int, input().split())))

X = int(input())

V = []
m = 100
for i, a in enumerate(A, 1):
    if X in a:
        m = min(m, len(a))
        V.append((i, len(a)))

ans = [i for i, l in V if l == m]
print(len(ans))
print(*ans)
