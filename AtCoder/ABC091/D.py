N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0

for i in range(30):
    p = 1 << i
    q = p - 1

    A0 = []
    A1 = []
    B0 = []
    B1 = []

    for v in A:
        if v & p:
            A1.append(v & q)
        else:
            A0.append(v & q)

    for v in B:
        if v & p:
            B1.append(v & q)
        else:
            B0.append(v & q)

    A0.sort(reverse=True)
    A1.sort(reverse=True)
    B0.sort()
    B1.sort()

    L0 = len(B0)
    L1 = len(B1)

    B0.append(p)
    B1.append(p)

    cnt = 0

    n0 = 0
    n1 = 0
    for v in A0:
        while v + B0[n0] < p:
            n0 += 1
        while v + B1[n1] < p:
            n1 += 1

        cnt += L0 - n0
        cnt += n1

    n0 = 0
    n1 = 0
    for v in A1:
        while v + B0[n0] < p:
            n0 += 1
        while v + B1[n1] < p:
            n1 += 1

        cnt += n0
        cnt += L1 - n1

    if cnt % 2:
        ans += p

print(ans)
