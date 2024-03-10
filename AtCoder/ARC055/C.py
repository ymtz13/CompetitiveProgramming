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


def solve(S):
    ZL = z_algo(S)
    ZR = z_algo(S[::-1])[::-1]

    ans = 0
    for i in range(3, len(S) - 1):
        nL = i
        nR = len(S) - i
        if nL < nR + 1:
            continue

        za = ZL[i]
        zc = ZR[i - 1]

        if za + zc < nR:
            continue

        a = min(nR - 1, za + zc - nR + 1, za, zc)
        ans += a

    return ans


def naive(S):
    ans = 0
    for nAC in range(2, len(S)):
        nB = len(S) - nAC * 2
        if nB <= 0:
            break

        for nA in range(1, nAC):
            nC = nAC - nA

            A = S[:nA]
            B = S[nA : nA + nB]
            C = S[-nC:]

            if A + B + C + A + C == S:
                ans += 1

    return ans


# for s in range(1 << 16):
#     s = f"{s:016b}"
#     ans = solve(s)
#     nav = naive(s)
#     if ans != nav:
#         print(s, ans, nav)
#         input()


S = input()
ans = solve(S)
print(ans)
