def solve(N, P):
    if P == sorted(P):
        return 0

    S = set()
    mex = 1
    for i, p in enumerate(P, 1):
        S.add(p)
        while mex in S:
            mex += 1

        if i == p and mex > i:
            return 1

    if P[0] == N and P[-1] == 1:
        return 3

    return 2


T = int(input())
for _ in range(T):
    N = int(input())
    P = list(map(int, input().split()))

    print(solve(N, P))
