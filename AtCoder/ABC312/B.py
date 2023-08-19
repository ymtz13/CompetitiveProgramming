H, W = map(int, input().split())
S = [input() for _ in range(H)]

ans = []

for h0 in range(H - 8):
    for w0 in range(W - 8):
        isValid = True
        for dh in range(3):
            for dw in range(3):
                if S[h0 + dh][w0 + dw] == ".":
                    isValid = False
                if S[h0 + dh + 6][w0 + dw + 6] == ".":
                    isValid = False

        for d in range(3):
            if S[h0 + d][w0 + 3] == "#":
                isValid = False
            if S[h0 + 3][w0 + d] == "#":
                isValid = False
            if S[h0 + d + 6][w0 + 5] == "#":
                isValid = False
            if S[h0 + 5][w0 + d + 6] == "#":
                isValid = False
        if S[h0 + 3][w0 + 3] == "#":
            isValid = False
        if S[h0 + 5][w0 + 5] == "#":
            isValid = False

        if isValid:
            ans.append((h0 + 1, w0 + 1))

ans.sort()
for h, w in ans:
    print(h, w)
