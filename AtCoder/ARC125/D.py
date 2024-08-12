mod = 998244353

N = int(input())
A = list(map(int, input().split()))


def solve(A):
    S = 1
    D = [0] * (N + 1)
    ans = [0] * (N + 1)

    for a in A:
        p = D[a]

        v = S - p
        v %= mod

        S += v - p
        S %= mod

        D[a] = v

        print(S, D)

        ans[a] = v

    print(ans)
    # print(sum(ans))

    return sum(ans)


def naive(A):
    S = set()
    D = set()
    for b in range(1, 1 << len(A)):
        t = tuple([a for i, a in enumerate(A) if (b >> i) & 1])
        if t in S:
            D.add(t)
        S.add(t)

    A = S.difference(D)
    print(A)

    return len(A)


a0 = solve(A)
a1 = naive(A)

print(a0, a1)

# 1 2 1 3  o
# 1 2 1    o
# 1 2   3  o
# 1 2      o
# 1   1 3  o
# 1   1    o
# 1     3  x
# 1        x
#   2 1 3  o
#   2 1    o
#   2   3  o
#   2      o
#     1 3  x
#     1    x
#       3  o
