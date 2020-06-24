N = int(input())
A = []
for _ in range(N):
    X, L = map(int, input().split())
    A.append((X-L, X+L))

A = sorted(A, key=lambda x:x[1])
p = -10**10
ans = 0
for l, r in A:
    if l>=p:
        ans += 1
        p = r
print(ans)
