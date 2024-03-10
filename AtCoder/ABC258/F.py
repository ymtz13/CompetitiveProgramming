T = int(input())

ans = []
for _ in range(T):
    B, K, Sx, Sy, Gx, Gy = map(int, input().split())

    Sl = (Sx // B) * B
    Gl = (Gx // B) * B
    Sd = (Sy // B) * B
    Gd = (Gy // B) * B
    Sr = Sl + B
    Gr = Gl + B
    Su = Sd + B
    Gu = Gd + B

    S = [
        ((Sl, Sy), abs(Sx - Sl) * K, "y"),
        ((Sr, Sy), abs(Sx - Sr) * K, "y"),
        ((Sx, Sd), abs(Sy - Sd) * K, "x"),
        ((Sx, Su), abs(Sy - Su) * K, "x"),
    ]

    G = [
        ((Gl, Gy), abs(Gx - Gl) * K, "y"),
        ((Gr, Gy), abs(Gx - Gr) * K, "y"),
        ((Gx, Gd), abs(Gy - Gd) * K, "x"),
        ((Gx, Gu), abs(Gy - Gu) * K, "x"),
    ]

    a = abs(Sx - Gx) * K + abs(Sy - Gy) * K

    for (sx, sy), ts, ds in S:
        for (gx, gy), tg, dg in G:
            if ds != dg:
                t = abs(sx - gx) + abs(sy - gy)

            if ds == "x" and dg == "x":
                t = 1 << 60
                if sy == gy:
                    t = abs(Sx - Gx)
                for x in (Sl, Sr, Gl, Gr):
                    t = min(t, abs(Sx - x) + abs(Gx - x))
                t += abs(sy - gy)

            if ds == "y" and dg == "y":
                t = 1 << 60
                if sx == gx:
                    t = abs(Sy - Gy)
                for y in (Sd, Su, Gd, Gu):
                    t = min(t, abs(Sy - y) + abs(Gy - y))
                t += abs(sx - gx)

            t += ts + tg
            a = min(a, t)

    ans.append(a)


for a in ans:
    print(a)
