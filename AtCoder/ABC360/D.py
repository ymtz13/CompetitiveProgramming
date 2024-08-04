N, T = map(int, input().split())
S = input()
X = list(map(int, input().split()))

E = []
for i, c in enumerate(S):
    x = X[i]
    if c == "0":
        E.append((x, i, 0, None))
    else:
        E.append((x, i, 1, True))
        E.append((x + T * 2 + 0.5, i, 1, False))

E.sort()

cnt = 0
ans = [0] * N

for _, i, d, start in E:
    if d == 0:
        cnt += 1
    else:
        if start:
            ans[i] -= cnt
        else:
            ans[i] += cnt

print(sum(ans))
