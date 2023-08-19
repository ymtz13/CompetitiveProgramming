N = int(input())
S0 = 0
D = []
for _ in range(N):
    A, B = map(int, input().split())
    D.append(B - A)
    S0 += A

D.sort(reverse=True)

ans = D[0] if N % 2 == 1 else 0
s = 0
for n, d in enumerate(D, 1):
    s += d
    if n % 2 == N % 2:
        ans = max(ans, s)

ans += S0
print(ans)
