H, W = map(int, input().split())
H2 = H + 2
W2 = W + 2

M = ["." * W2] + [".{}.".format(input()) for _ in range(H)] + ["." * W2]

ans = [0] * (min(H, W) + 1)

for h in range(1, H + 1):
    for w in range(1, W + 1):
        if "." in (
            M[h][w],
            M[h + 1][w + 1],
            M[h + 1][w - 1],
            M[h - 1][w + 1],
            M[h - 1][w - 1],
        ):
            continue

        for d in range(110):
            if M[h + d][w + d] == ".":
                break

        ans[d - 1] += 1

print(*ans[1:])
