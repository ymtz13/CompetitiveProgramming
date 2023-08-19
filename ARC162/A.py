T = int(input())
ans = []

for _ in range(T):
    N = int(input())
    P = list(enumerate(map(int, input().split())))

    a = 0
    for i1, p1 in P:
        f = True
        for i2, p2 in P:
            if i1 < i2 and p1 > p2:
                f = False
        if f:
            a += 1

    ans.append(a)


for a in ans:
    print(a)
