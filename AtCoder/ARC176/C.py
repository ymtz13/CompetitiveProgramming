mod = 998244353


def solve(N, M, edges):
    E = [[] for _ in range(N + 1)]
    P = [[] for _ in range(N + 1)]

    for A, B, C in edges:
        E[A].append((B, C))
        E[B].append((A, C))
        P[C].append((A, B))

    Confirmed = [0] * (N + 1)
    UpperBound = [N] * (N + 1)
    Pairs = [None] * (N + 1)

    for i, ee in enumerate(E[1:], 1):
        if not ee:
            continue

        cmin = min([c for _, c in ee])
        jcmin = []

        for j, c in ee:
            if c > cmin:
                # j は c で確定する
                if Confirmed[j] and Confirmed[j] != c:
                    return 0
                if UpperBound[j] < c:
                    return 0
                Confirmed[j] = c
                UpperBound[j] = c
            else:
                UpperBound[j] = min(UpperBound[j], c)
                if Confirmed[j] > c:
                    return 0

                jcmin.append(j)

        UpperBound[i] = min(UpperBound[i], cmin)
        if Confirmed[i] > cmin:
            return 0

        if len(jcmin) >= 2:
            # i は cmin で確定する
            if Confirmed[i] and Confirmed[i] != cmin:
                return 0
            Confirmed[i] = cmin
        else:
            k = jcmin[0]
            if (
                k < i
                and not Confirmed[i]
                and not Confirmed[k]
                and UpperBound[i] == cmin
                and UpperBound[k] == cmin
            ):
                Pairs[cmin] = (k, i)

    for c, pp in enumerate(P[1:], 1):
        if not pp:
            continue
        a, b = pp[0]

        fa = all([a in p for p in pp])
        fb = all([b in p for p in pp])

        if not fa and not fb:
            return 0

    # print(Confirmed)
    # print(UpperBound)
    # print(Pairs)

    cub = [0] * (N + 1)
    for ub in UpperBound[1:]:
        cub[ub] += 1
    # print(cub)

    used = set()
    for c in Confirmed[1:]:
        used.add(c)
        if c:
            cub[c] -= 1

    ans = 1
    for i, p in enumerate(Pairs[1:], 1):
        if p:
            ans *= 2
            ans %= mod
            used.add(i)
            cub[i] -= 1

    # print(cub)

    # ans = pow(2, len(Pairs), mod)
    # print(ans, Pairs)
    cnt = 0
    # print(used)
    for i in range(1, N + 1):
        # print(i, cnt)
        if i not in used:
            cnt += 1

        for _ in range(cub[i]):
            if cnt == 0:
                return 0

            ans *= cnt
            ans %= mod
            cnt -= 1

    return ans


N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]

a = solve(N, M, edges)
print(a)
