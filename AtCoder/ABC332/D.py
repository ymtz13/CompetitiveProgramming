from itertools import permutations

H, W = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in range(H)]
B = [tuple(map(int, input().split())) for _ in range(H)]

ans = 10000

for PH in permutations(range(H)):
    cH = 0
    for i, v in enumerate(PH):
        for w in PH[:i]:
            if w > v:
                cH += 1

    for PW in permutations(range(W)):
        cW = 0
        for i, v in enumerate(PW):
            for w in PW[:i]:
                if w > v:
                    cW += 1

        ok = True
        for h, ph in enumerate(PH):
            for w, pw in enumerate(PW):
                if A[h][w] != B[ph][pw]:
                    ok = False
                    break
            if not ok:
                break

        if ok:
            ans = min(ans, cH + cW)

print(ans if ans < 10000 else -1)
