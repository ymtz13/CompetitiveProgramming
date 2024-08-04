N = int(input()) + 1

A = []
while N:
    A.append(N % 10)
    N //= 10
A.reverse()

ans = 0
s = 0
n = len(A) - 1
for d in A:
    if d > 0:
        ans = max(ans, s + d - 1 + 9 * n)

    s += d
    n -= 1

print(ans)
