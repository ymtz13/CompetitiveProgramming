T = int(input())
cases = [int(input()) for _ in range(T)]
ans = []

for N in cases:
    a = 0

    for b in range(2, 101):
        n = N
        ok = True
        while n:
            if n % b > 1:
                ok = False
                break
            n //= b
        if ok:
            a += 1

    ng = N + 1
    for x in range(1, 1 << 10):
        ok = 0
        while ng - ok > 1:
            t = (ng + ok) // 2
            s = sum([t**i for i in range(10) if (x >> i) & 1])
            if s <= N:
                ok = t
            else:
                ng = t

        s = sum([ok**i for i in range(10) if (x >> i) & 1])
        # print(f"{x:010b}", ok, s, ng)

        if s == N and ok > 100:
            a += 1

    ans.append(a)

for a in ans:
    print(a)
