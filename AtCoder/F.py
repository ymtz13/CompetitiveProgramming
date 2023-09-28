INF = 1 << 70

N = int(input())
X = [x * 2 for x in map(int, input().split())]
L = [x * 2 for x in map(int, input().split())]

P = [-INF, INF]
for i, l in enumerate(X):
    P.append(l)
    for r in X[i + 1 :]:
        P.append((l + r) // 2)
P = sorted(list(set(P)))

# print(P)

ans = 0
for p, q in zip(P, P[1:]):
    p += 1
    # print(p, q)

    # D = [(abs(p - x), 1 if x >= p else -1) for x in X]
    # D.sort()
    D = sorted(X, key=lambda x: abs(p - x))

    Llim = p
    Rlim = q
    for x, length in zip(D, L):
        ll = x - length
        rr = x + length

        Llim = max(Llim, ll)
        Rlim = min(Rlim, rr)

    if Llim % 2:
        Llim += 1
    if Rlim % 2:
        Rlim -= 1

    a = max(0, Rlim // 2 - Llim // 2 + 1)
    ans += a
    # print("[{},{}]".format(p, q), Llim, Rlim, a)

print(ans)
