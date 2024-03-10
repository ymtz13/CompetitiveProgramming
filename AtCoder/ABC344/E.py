from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(Q)]

Anext = defaultdict(int)
Aprev = defaultdict(int)

head = -1
tail = -2
Anext[head] = A[0]
Aprev[A[0]] = head
Anext[A[-1]] = tail
Aprev[tail] = A[-1]


def p():
    i = head
    ret = []
    while i != tail:
        i = Anext[i]
        ret.append(i)

    return ret


for a, anxt in zip(A, A[1:]):
    Anext[a] = anxt
    Aprev[anxt] = a

for query in queries:
    if query[0] == 1:
        _, x, y = query
        xnxt = Anext[x]

        Anext[x] = y
        Anext[y] = xnxt
        Aprev[y] = x
        Aprev[xnxt] = y

    else:
        _, x = query
        xprv = Aprev[x]
        xnxt = Anext[x]
        Anext[xprv] = xnxt
        Aprev[xnxt] = xprv

print(*p()[:-1])
