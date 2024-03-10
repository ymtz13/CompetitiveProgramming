from z_algo import z_algo


def naive(S: str):
    L = len(S)
    ret = []
    for i in range(L):
        v = 0
        for j in range(L - i):
            if S[j] != S[i + j]:
                break
            v += 1
        ret.append(v)
    return ret


cmpmax = 0
for s in range(1 << 16):
    s = f"{s:016b}"

    ret_naive = naive(s)
    ret_zalgo = z_algo(s)

    if ret_naive != ret_zalgo:
        print(s)
        print(ret_naive)
        print(ret_zalgo)

    assert ret_naive == ret_zalgo

print(cmpmax)
