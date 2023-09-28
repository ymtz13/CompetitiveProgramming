from itertools import product

N = int(input())
E = [[0] * N for _ in range(N)]
# E2 = [[0] * N for _ in range(N)]

for i in range(N - 1):
    D = list(map(int, input().split()))

    for j, d in enumerate(D, i + 1):
        E[i][j] = E[j][i] = d
        # E2[N - 1 - i][N - 1 - j] = E2[N - 1 - j][N - 1 - i] = d


def solve(E):
    if N % 2:
        R = [range(i) for i in range(N - 2, 0, -2)]
    else:
        R = [range(i) for i in range(N - 1, 0, -2)]

    ans = 0

    for skip in range(N):
        if N % 2 == 0 and skip > 0:
            break

        for p in product(*R):
            U = list(range(N))
            if N % 2:
                U.pop(skip)
            S = 0

            # pairs = []
            for i in p:
                l = U.pop(0)
                r = U.pop(i)
                S += E[l][r]
                # pairs.append((l, r))

            ans = max(ans, S)
            # print(pairs, S)

    return ans


print(solve(E))
