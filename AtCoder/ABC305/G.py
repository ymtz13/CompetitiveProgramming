mod = 998244353

N, M = map(int, input().split())
S = [input() for _ in range(M)]

if N <= 6:
    ans = 1 << N
    for x in range(1 << N):
        X = "".join(["b" if x & (1 << b) else "a" for b in range(N)])

        for s in S:
            if s in X:
                ans -= 1
                break

    print(ans)
    exit()

vec = []
for x in range(1 << 6):
    X = "".join(["b" if x & (1 << b) else "a" for b in range(6)])

    v = 1
    for s in S:
        if s in X:
            v = 0
            break

    vec.append(v)

for x, v in enumerate(vec):
    X = "".join(["b" if x & (1 << b) else "a" for b in range(6)])


mat = [[0] * 64 for _ in range(64)]
for i, v in enumerate(vec):
    if v == 0:
        continue
    j = i % 32
    mat[i][j * 2] = mat[i][j * 2 + 1] = 1


def matsq(mat):
    D = len(mat)
    ret = [[0] * D for _ in range(D)]
    for i in range(D):
        for j in range(D):
            for k in range(D):
                ret[i][j] += mat[i][k] * mat[k][j]
                ret[i][j] %= mod

    return ret


def apply(mat, vec):
    D = len(mat)
    ret = []
    for i in range(D):
        v = 0
        for j in range(D):
            v += mat[i][j] * vec[j]
            v %= mod
        ret.append(v)
    return ret


P = N - 6
for i in range(60):
    if P & (1 << i):
        vec = apply(mat, vec)
    mat = matsq(mat)

ans = 0
for v in vec:
    ans += v
    ans %= mod

print(ans)
