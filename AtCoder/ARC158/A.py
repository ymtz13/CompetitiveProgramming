T = int(input())

ans = []
for _ in range(T):
    x = tuple(map(int, input().split()))
    s = sum(x)

    if s % 3:
        ans.append(-1)
        continue

    a = s // 3
    d = sorted([v - a for v in x])

    ok = True
    for v in d:
        if v % 2:
            ok = False
            break
    if not ok:
        ans.append(-1)
        continue

    if d[1] > 0:
        ans.append(-d[0] // 2)
    else:
        ans.append(d[2] // 2)

for a in ans:
    print(a)
