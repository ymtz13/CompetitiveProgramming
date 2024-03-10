H, W, N = map(int, input().split())
T = input()
HW = H * W

X = set([0])
x = 0
for t in T:
    if t == "L":
        x -= 1
    if t == "R":
        x += 1
    if t == "U":
        x -= W
    if t == "D":
        x += W
    X.add(x)


B = []
for h in range(H):
    S = input()
    for c in S:
        B.append(1 if c == "." else 0)

ans = 0
for h in range(1, H - 1):
    for w in range(1, W - 1):
        s = h * W + w

        ok = True
        for x in X:
            i = s + x
            if not 0 <= i < HW or not B[i]:
                ok = False
                break

        if ok:
            ans += 1

print(ans)
