T = int(input())
ans = []

for _ in range(T):
    N = int(input())
    if N < 7:
        ans.append(-1)
        continue
    if N == 7:
        ans.append(7)
        continue

    B = [(N >> i) & 1 for i in range(60, -1, -1)]
    I = []
    for i, b in enumerate(B):
        if b == 1:
            I.append(i)

    if len(I) >= 3:
        X = I[:3]

    if len(I) == 2:
        i0 = I[0]
        i1 = I[1]
        X = [i0, i1 + 1, i1 + 2] if i1 + 2 <= 60 else [i0 + 1, i0 + 2, i0 + 3]

    if len(I) == 1:
        i0 = I[0]
        X = [i0 + 1, i0 + 2, i0 + 3]

    a = 0
    for x in X:
        a += 1 << (60 - x)
    ans.append(a)


for a in ans:
    print(a)
