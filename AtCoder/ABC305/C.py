H, W = map(int, input().split())
S = ["." * (W + 2)] + ["." + input() + "." for _ in range(H)] + ["." * (W + 2)]

for ih, row in enumerate(S[1 : H + 1], 1):
    for iw, c in enumerate(row[1 : W + 1], 1):
        if c == "#":
            continue

        cnt = 0
        for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            if S[ih + dh][iw + dw] == "#":
                cnt += 1

        if cnt >= 2:
            print(ih, iw)
            exit()
