from random import shuffle, seed

# seed(1020)

# N = 20
# E = [(i, j) for i in range(1, N + 1) for j in range(i + 1, N + 1)]
# shuffle(E)

N = int(input())
E = [tuple(map(int, input().split())) for _ in range(N * (N - 1) // 2)]


def solve(N, E):
    V = [[10**8 if i == j else 0 for i in range(N)] for j in range(N)]

    for n, (a, b) in enumerate(E[::-1]):
        a -= 1
        b -= 1

        d = n + 100
        dsq = d * d
        V[a][b] += dsq
        V[b][a] += dsq

    return V


def distsq(v1, v2):
    sq = 0
    for c1, c2 in zip(v1, v2):
        sq += (c2 - c1) ** 2
    return sq


def distmat(V):
    ret = []
    for i in range(N):
        for j in range(i + 1, N):
            ret.append((i + 1, j + 1, distsq(V[i], V[j])))
    return ret


V = solve(N, E)

# res = distmat(V)
# res.sort(key=lambda x: x[2])
# for e, r in zip(E, res):
#     print(e, r)
#     if e != (r[0], r[1]):
#         print("XXXXXXX")
#         input()
# exit()

for v in V:
    print(*v)
