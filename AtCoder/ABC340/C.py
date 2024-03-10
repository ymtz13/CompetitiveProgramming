from sys import setrecursionlimit

setrecursionlimit(1 << 20)

memo = {}


def dfs(x):
    if x == 1:
        return 0
    if x in memo:
        return memo[x]

    l = x // 2
    r = x - l

    v = x + dfs(l) + dfs(r)
    memo[x] = v
    return v


N = int(input())


print(dfs(N))
