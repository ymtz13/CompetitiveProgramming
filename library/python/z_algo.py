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
