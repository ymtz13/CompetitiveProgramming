from sys import setrecursionlimit

setrecursionlimit(10000000)

mod = 998244353
inv2 = pow(2, mod - 2, mod)

ans = {}


def dfs(S, i, v):
    if len(S) == 1:
        ans[S[0]] = v
        return

    X = [[] for _ in range(27)]
    for s in S:
        X[ord(s[i]) - 96].append(s)

    M0 = len(X[0])
    MX = len(S) - M0

    for s in X[0]:
        ans[s] = v

    for x in X[1:]:
        if x:
            vv = v + M0 + (MX - len(x)) * inv2
            vv %= mod
            dfs(x, i + 1, vv)


N = int(input())
S = [input() + "`" for _ in range(N)]

dfs(S, 0, 1)

for s in S:
    print(ans[s])
