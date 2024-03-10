N = int(input())
A = list(map(int, input().split()))

Z = 0

for i in range(62):
    b = 1 << i

    cnt = 0
    for a in A:
        if a & b:
            cnt += 1

    if cnt & 1:
        Z += b
        A = [a - (a & b) for a in A]


C = []
for i in range(61, -1, -1):
    b = 1 << i
    for a in A:
        for j, c in C:
            bj = 1 << j
            if a & bj:
                a ^= c

        if b & a:
            C = [(j, c ^ a if c & b else c) for j, c in C]
            C.append((i, a))
            break


def ok(x):
    r = 0
    for j, c in C:
        b = 1 << j
        if x & b:
            r ^= c

    return x <= r


X = 0
for i in range(61, -1, -1):
    b = 1 << i

    if ok(X + b):
        X += b

print(X * 2 + Z)
