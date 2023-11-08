H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

T = []
for row in A:
    t = [0]
    for a in row:
        t.append(t[-1] + a)
    T.append(t)

S = [[0] * (W + 1)]
for row in T:
    S.append(S[-1][:])
    s = S[-1]
    for i, t in enumerate(row):
        s[i] += t

# print(S)


def cnt(h1, w1, h2, w2):
    h0 = h1 - 1
    w0 = w1 - 1
    return S[h2][w2] - S[h2][w0] - S[h0][w2] + S[h0][w0]


ans = -1
for h0 in range(1, H + 1):
    for w0 in range(1, W + 1):
        s0 = cnt(1, 1, h0, w0)

        ok = True

        hp = h0 + 1
        Lh = [h0]
        for h in range(h0 + 1, H + 1):
            s = cnt(hp, 1, h, w0)
            if s > s0:
                ok = False
                break
            if s == s0:
                hp = h + 1
                Lh.append(h)

        if hp != H + 1:
            ok = False
        if not ok:
            continue

        wp = w0 + 1
        Lw = [w0]
        for w in range(w0 + 1, W + 1):
            s = cnt(1, wp, h0, w)
            if s > s0:
                ok = False
                break
            if s == s0:
                wp = w + 1
                Lw.append(w)

        if wp != W + 1:
            ok = False
        if not ok:
            continue

        for hp, hq in zip(Lh, Lh[1:]):
            for wp, wq in zip(Lw, Lw[1:]):
                s = cnt(hp + 1, wp + 1, hq, wq)
                if s != s0:
                    ok = False
                    break

        if ok:
            ans += 1

        # print(Lh, Lw)

print(ans)
