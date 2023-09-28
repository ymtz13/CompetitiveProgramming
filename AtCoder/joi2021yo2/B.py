N, Q = map(int, input().split())
A = 0
B = 1
C = 2
oA = ord("A")


def toTuple(x):
    ret = []
    for _ in range(N):
        ret.append(x & 0b11)
        x >>= 2
    return tuple(ret[::-1])


def toValue(t):
    ret = 0
    for v in t:
        ret <<= 2
        ret += v
    return ret


def strToValue(s):
    ret = 0
    for c in s:
        ret <<= 2
        ret += ord(c) - oA
    return ret


def flip(t, n):
    return t[:n][::-1] + t[n:]


mask = [0b11 << x * 2 for x in range(N)]


def flipV(v, n):
    ret = v
    for i in range(n):
        l = N - i - 1
        r = N - n + i

        # vr = (v >> (r * 2)) & 0b11
        # ret -= v & (0b11 << (l * 2))
        # ret += vr << (l * 2)

        m = mask[l]
        vr = (v >> (r * 2)) << (l * 2)
        ret -= v & m
        ret += vr & m

    return ret


def flipVlist(v):
    P = [v & m for m in mask]
    Q = [p >> (i * 2) for i, p in enumerate(P)]

    result = []
    for n in range(2, N + 1):
        ret = v
        for i in range(n):
            l = N - i - 1
            r = N - n + i

            # m = mask[l]
            # vr = (v >> (r * 2)) << (l * 2)
            vr = Q[r] << (l * 2)
            # ret -= v & m
            ret -= P[l]
            ret += vr
            # ret += vr & m

        result.append(ret)

    return result


M = 4**N
X = [-1] * M
cnt = 0

T = []
for nA in range(N + 1):
    for nB in range(N - nA + 1):
        nC = N - nA - nB
        t = (A,) * nA + (B,) * nB + (C,) * nC
        v = toValue(t)
        T.append(v)
        X[v] = 0
        cnt += 1

dist = 1

while cnt < 3**N:
    T_next = []
    for t in T:
        for u in flipVlist(t):
            if X[u] == -1:
                X[u] = dist
                T_next.append(u)
                cnt += 1

    dist += 1
    T = T_next

ans = []
for _ in range(Q):
    s = input()
    ans.append(X[strToValue(s)])

for a in ans:
    print(a)
