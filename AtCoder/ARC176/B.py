def solve(N, M, K):
    if M - K == 1:
        if N >= K:
            return 0
        else:
            return [2, 4, 8, 6][(N - 1) % 4]

    if M >= N + 1:
        return [2, 4, 8, 6][(N - 1) % 4]

    Q = (N - M) // (M - K)
    X = N - (Q + 1) * (M - K)

    if X == 0:
        return 1

    return [2, 4, 8, 6][(X - 1) % 4]


def naive(N, M, K):
    n = pow(2, N)
    m = pow(2, M)
    k = pow(2, K)
    return n % (m - k) % 10


# from random import randint, seed

# seed(1)
# for _ in range(1000):
#     N = randint(1, 1000)
#     M = randint(2, 1000)
#     K = randint(1, M - 1)
#     s = solve(N, M, K)
#     n = naive(N, M, K)
#     # print((s, n, (N, M, K)))
#     assert s == n, (s, n, (N, M, K))

# exit()

T = int(input())

ans = []
for _ in range(T):
    N, M, K = map(int, input().split())
    a = solve(N, M, K)
    ans.append(a)

for a in ans:
    print(a)
