Q = int(input())
Queries = [tuple(map(int, input().split())) for _ in range(Q)]

M = 31
D = [M]
Child0 = [None]
Child1 = [None]
Parent = [None]
Cnt = [0]
Value = [0]


Ans = []
for query in Queries:
    t = query[0]

    if t == 1:
        x = query[1]

        i = 0
        Cnt[i] += 1
        for d in range(M - 1, -1, -1):
            b = x & (1 << d)
            if b == 0:
                if Child0[i] is None:
                    idx = len(D)
                    D.append(d)
                    Child0.append(None)
                    Child1.append(None)
                    Parent.append(i)
                    Cnt.append(0)
                    Value.append(0)
                    Child0[i] = idx
                ichild = Child0[i]
            else:
                if Child1[i] is None:
                    idx = len(D)
                    D.append(d)
                    Child0.append(None)
                    Child1.append(None)
                    Parent.append(i)
                    Cnt.append(0)
                    Value.append(0)
                    Child1[i] = idx
                ichild = Child1[i]
            Cnt[ichild] += 1
            i = ichild

        print(Child0)
        print(Child1)
        print(Parent)

    if t == 2:
        x = query[1]

    if t == 3:
        Ans.append(Value[0])

for a in Ans:
    print(a)
