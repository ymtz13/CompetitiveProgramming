K = int(input())
N = int(input())
AD = [tuple(map(int, input().split())) for _ in range(N)]

# 10 + 13 + 16
# 12 + 16
# 15
# 82

# 10 + 13
# 12
# 15
#


def f(M):
    # A + (n-1)D <= M
    # (n-1)D <= M - A
    # n <= (M-A)//D + 1

    k = s = 0
    for A, D in AD:
        n = max(0, (M - A) // D + 1)
        k += n
        s += A * n + D * (n - 1) * n // 2
        # print(A, D, n)

    # print(M, s, k, s - (k - K) * M)

    return s - (k - K) * M if k >= K else None


ok = 1 << 70
ng = 0
while ok - ng > 1:
    tgt = (ok + ng) // 2

    r = f(tgt)
    if r is not None:
        ok = tgt
        ans = r
    else:
        ng = tgt

print(ans)
