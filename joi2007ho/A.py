N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]

s = sum(A[: K - 1])
ans = -(1 << 60)

for a, b in zip(A[K - 1 :], A):
    s += a
    ans = max(ans, s)
    s -= b

print(ans)
