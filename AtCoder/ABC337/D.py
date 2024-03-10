H, W, K = map(int, input().split())
S = [[0 if c == "." else 1 if c == "o" else 2 for c in input()] for _ in range(H)]

INF = H + W + 10


def rot(S):
    return list(zip(*S))[::-1]


def f(S):
    r = INF
    for X in S:
        Cd = [0]
        # Co = [0]
        Cx = [0]
        cd = cx = 0

        for i, x in enumerate(X, 1):
            if x == 0:
                cd += 1
            if x == 2:
                cx += 1
            Cd.append(cd)
            Cx.append(cx)

            if i >= K:
                v_ = Cd[-1] - Cd[-1 - K]
                vx = Cx[-1] - Cx[-1 - K]

                if vx == 0:
                    r = min(r, v_)

    return r


S0 = S
S1 = rot(S0)
S2 = rot(S1)
S3 = rot(S2)

ans = min(f(S0), f(S1), f(S2), f(S3))
print(ans if ans < INF else -1)
