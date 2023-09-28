H, W = map(int, input().split())
ans = []

for _ in range(H):
    a = []
    x = -1
    S = input()

    for c in S:
        if x >= 0:
            x += 1
        if c == "c":
            x = 0
        a.append(x)

    ans.append(a)

for a in ans:
    print(*a)
