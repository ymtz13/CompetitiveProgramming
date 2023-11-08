N = int(input())
A = sorted([int(input()) for _ in range(N)])
B = [i for i in range(1, 2 * N + 1) if i not in A]


def pick(X, v):
    for x in X:
        if x > v:
            return x

    return None


t = 0
v = 0
while A and B:
    if t == 0:
        x = pick(A, v)
        if x is not None:
            v = x
            A.remove(x)
        else:
            v = 0
    else:
        x = pick(B, v)
        if x is not None:
            v = x
            B.remove(x)
        else:
            v = 0

    t = 1 - t

print(len(B))
print(len(A))
