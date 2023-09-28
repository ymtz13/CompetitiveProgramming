N, M = map(int, input().split())
C = []

for _ in range(N):
    S = input()
    C.append((S.count("W"), S.count("B"), S.count("R")))

ans = 0
for nW in range(1, N - 1):
    for nB in range(1, N - nW):
        nR = N - nW - nB

        c = 0
        for i, (cW, cB, cR) in enumerate(C):
            if i < nW:
                c += cW
            elif i < nW + nB:
                c += cB
            else:
                c += cR

        ans = max(ans, c)


print(N * M - ans)
