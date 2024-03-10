N = int(input())
S = input()

X = []

s = 0
for c in S:
    if c == ">":
        s += 1
    else:
        if s > 0:
            X.append(s)
            s = 0

if s > 0:
    X.append(s)


ans = 0
for x in X:
    ans += (x + 1) * x // 2

print(ans)
