H, W = map(int, input().split())

ans = []
for _ in range(H):
    S = input()
    R = []
    cnt = 0
    for c in S:
        R.append(c)

        if c == ".":
            cnt = 0
        else:
            if cnt == 0:
                cnt = 1
            else:
                cnt = 0
                R.pop()
                R.pop()
                R.extend(["P", "C"])

    ans.append("".join(R))

for a in ans:
    print(a)
