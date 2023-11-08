N = int(input())
K = int(input())

ans = []

for _ in range(K):
    a, b = map(int, input().split())

    l = a - 1
    r = N - a
    u = b - 1
    d = N - b
    m = min(l, r, u, d)

    ans.append(m % 3 + 1)

for a in ans:
    print(a)
