N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = [max(a, b) * M for a, b in zip(A, B)]

IABC = tuple([(max(a, b), b, c) for a, b, c in zip(A, B, C)])


def possible(X):
    free = 0
    need = 0
    for maxab, b, c in IABC:
        if c < X:
            need += (X - c + b - 1) // b
        else:
            free += (c - X) // maxab

    return free >= need


ok = 0
ng = max(C) * N + 1

while ng - ok > 1:
    tgt = (ng + ok) // 2
    if possible(tgt):
        ok = tgt
    else:
        ng = tgt

print(ok)
