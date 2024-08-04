def z_algo(S: str):
    L = len(S)
    ret = [L]
    i = 1
    jnxt = 0
    while i < L:
        j = jnxt
        while i + j < L and S[j] == S[i + j]:
            j += 1

        ret.append(j)

        jnxt = 0
        for k in range(1, j):
            if k + ret[k] >= j:
                jnxt = j - k
                break
            ret.append(ret[k])

        i = len(ret)

    return ret


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

INF = 1 << 60
ans = [0] * N

for i in range(32):
    bit = 1 << i
    AA = [a & bit for a in A]

    B0 = [b & bit for b in B]
    B1 = [bit - b for b in B0]

    X0 = B0 + [-1] + AA + AA
    X1 = B1 + [-1] + AA + AA

    Z0 = z_algo(X0)[N + 1 : N * 2 + 1]
    Z1 = z_algo(X1)[N + 1 : N * 2 + 1]

    for k, (z0, z1) in enumerate(zip(Z0, Z1)):
        if z1 == N:
            ans[k] += bit
        elif z0 != N:
            ans[k] = -INF


for k, x in enumerate(ans):
    if x < 0:
        continue
    print(k, x)
