N = int(input())
A = [int(input()) for _ in range(N)]
S = sum(A)
AA = A + A
NN = N + N


def check(X):
    s1 = s2 = 0
    i2 = 0
    for i1, a in enumerate(A):
        while s1 < X:
            if i2 == NN:
                return False
            s1 += AA[i2]
            i2 += 1

        s1 -= a

    return False


ok = 1
ng = 1 << 50
while ng - ok > 1:
    tgt = (ng + ok) // 2
    if check(tgt):
        ok = tgt
    else:
        ng = tgt

print(ok)
