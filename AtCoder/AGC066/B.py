x = 10**99
X = []
for i in range(100):
    X.append(x)
    x = x // 2

ans = [f"{X[50]}"]
for x in X[51:]:
    ans.append(f"{x:0100d}")

ans = "".join(ans)
print(ans)
