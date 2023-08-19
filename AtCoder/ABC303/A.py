N = int(input())
S = input()
T = input()

ans = True
for c1, c2 in zip(S, T):
    s = {c1, c2}

    if len(s) == 1 or s == {"1", "l"} or s == {"0", "o"}:
        continue
    ans = False

print("Yes" if ans else "No")
