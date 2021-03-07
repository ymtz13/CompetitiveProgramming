N = int(input())
D = []
for _ in range(N):
    A, B = map(int, input().split())
    D.append((A+B, A, B))

D = sorted(D, reverse=True)
ans = 0
for d, a, b in D[0::2]: ans += a
for d, a, b in D[1::2]: ans -= b
print(ans)