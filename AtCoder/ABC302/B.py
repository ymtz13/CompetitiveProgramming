H, W = map(int, input().split())

A = (
    ["_" * (W + 10)] * 5
    + ["_____{}_____".format(input()) for _ in range(H)]
    + ["_" * (W + 10)] * 5
)


for R in range(1, H + 1):
    for C in range(1, W + 1):
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                r = R + 4
                c = C + 4
                chars = [A[r + dr * i][c + dc * i] for i in range(5)]

                if chars == ["s", "n", "u", "k", "e"]:
                    for i in range(5):
                        print(R + dr * i, C + dc * i)
                    exit()
