N, M = map(int, input().split())
A = list(map(int, input().split()))

A1 = A[0]
A2 = A[1]
A = sorted(A[2:])

ans = 1 << 60
for i in range(N - M - 1):
    l = A[i]
    r = A[i + M - 1]

    vl = max(0, A1 - l)
    vr = max(0, r - A2)

    ans = min(ans, vl + vr)

print(ans)
