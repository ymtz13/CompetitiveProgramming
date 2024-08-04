T = int(input())
ans = []
for _ in range(T):
    K = int(input())
    a = 0

    X = []
    S = 0
    for n in range(1, 16):
        S += pow(9, n)
        if K <= S:
            break

    k = K - pow(9, n - 1)
    for v in range(1, 10):
        if k < v * pow(9, n - 1):
            break

    kk = k - (v - 1) * pow(9, n - 1) - 1
    print((n, v, k, kk))

    z = [] if kk else [0]
    while kk:
        z.append(kk % 9)
        kk //= 9
    z.append(v)
    z.reverse()
    print(z)

    p = 11
    a = []
    for zz in z:
        a.append(zz + 1 if p <= zz else zz)
        p = a[-1]

    ans.append(a)

for a in ans:
    print(a)
