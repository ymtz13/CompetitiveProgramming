N, M = map(int, input().split())
S = input()

m = M
X = x = 0

for c in S:
    if c == "0":
        m = M
        x = X

    if c == "1":
        if m > 0:
            m -= 1
        elif x > 0:
            x -= 1
        else:
            X += 1

    if c == "2":
        if x > 0:
            x -= 1
        else:
            X += 1

print(X)
