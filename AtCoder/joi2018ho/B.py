Z = 1000000010
N = int(input())

AB = []
for _ in range(N):
    a, b = map(int, input().split())
    AB.append(a * Z + b)
AB.sort()

X = []
D = []
s = 0

for ab in AB:
    a = ab // Z
    b = ab % Z

    s += b
    X.append(a + b - s)
    D.append(s - a)

M = []
m = -(1 << 60)
for d in reversed(D):
    m = max(m, d)
    M.append(m)
M.reverse()

ans = max(x + m for x, m in zip(X, M))
print(ans)
