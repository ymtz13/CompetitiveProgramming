mod = 998244353


def solve(N, A):
    E = set(A)

    for i, a in enumerate(A, 1):
        if a < i:
            return 0
        if i in E and i != a:
            return 0

    Q = [None] * (N + 1)
    S = set(range(1, N + 1))
    for i in range(N, 0, -1):
        a = A[i - 1]

        if Q[a] is not None:
            S.remove(Q[a])
        Q[a] = i

    V = [s * 10 for s in S]
    V.extend([e * 10 + 1 for e in E])
    V.sort()

    ans = 1
    cnt = 0
    for v in V:
        if v % 10:
            ans *= cnt
            ans %= mod
            cnt -= 1
        else:
            cnt += 1

    return ans


# N = 8
# A = [6, 6, 8, 4, 5, 6, 8, 8]
# print(solve(N, A))
# exit()

N = int(input())
A = list(map(int, input().split()))

ans = solve(N, A)
print(ans)
