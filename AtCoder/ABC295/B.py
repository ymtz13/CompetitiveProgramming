R, C = map(int, input().split())
B = [input() for _ in range(R)]

bombs = []
for r in range(R):
    for c in range(C):
        if B[r][c] != "." and B[r][c] != "#":
            bombs.append((r, c, int(B[r][c])))

ans = [[] for _ in range(R)]
for r in range(R):
    for c in range(C):
        if B[r][c] != "#":
            ans[r].append(".")
        else:
            f = False
            for br, bc, bb in bombs:
                d = abs(r - br) + abs(c - bc)
                if d <= bb:
                    f = True

            ans[r].append("." if f else "#")


for row in ans:
    print("".join(row))
