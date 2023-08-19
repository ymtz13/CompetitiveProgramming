HA, WA = map(int, input().split())
A = [[0 if c == "." else 1 for c in input()] for _ in range(HA)]
HB, WB = map(int, input().split())
B = [[0 if c == "." else 1 for c in input()] for _ in range(HB)]
HX, WX = map(int, input().split())
X = [[0 if c == "." else 1 for c in input()] for _ in range(HX)]


def shrink(A):
    hMin = wMin = 100
    hMax = wMax = 0
    for h, row in enumerate(A):
        for w, c in enumerate(row):
            if c:
                hMin = min(hMin, h)
                wMin = min(wMin, w)
                hMax = max(hMax, h)
                wMax = max(wMax, w)

    S = [row[wMin : wMax + 1] for row in A[hMin : hMax + 1]]
    return len(S), len(S[0]), S


def asum(A):
    return sum(map(sum, A))


HA, WA, A = shrink(A)
HB, WB, B = shrink(B)
HX, WX, X = shrink(X)


sumA = asum(A)
sumB = asum(B)
# print(sumA, sumB)

C0 = [[0] * 20 for _ in range(10)]
for arow in A:
    C0.append([0] * 10 + arow[:] + [0] * (10 - WA))
C0.extend([[0] * 20 for _ in range(10 - HA)])


# for r in C0:
#     print(r)

for h0 in range(20 - HB + 1):
    for w0 in range(20 - WB + 1):
        C = [c[:] for c in C0]
        for h, row in enumerate(B, h0):
            for w, b in enumerate(row, w0):
                C[h][w] += b

        # if h0 == 10 and w0 == 10:
        #     for r in C:
        #         print(r)

        for hx in range(20 - HX + 1):
            for wx in range(20 - WX + 1):
                S = [row[wx : wx + WX] for row in C[hx : hx + HX]]
                if asum(S) != sumA + sumB:
                    continue

                ok = True
                for rowX, rowS in zip(X, S):
                    for cX, cS in zip(rowX, rowS):
                        if bool(cX) != bool(cS):
                            ok = False
                            break
                    if not ok:
                        break

                if ok:
                    print("Yes")
                    exit()

print("No")
