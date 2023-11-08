N, M = map(int, input().split())

B = [[]] + [list(map(int, input().split())) + [None] * N for _ in range(M)]
HeightOf = [N // M] * (M + 1)

PileOf = [None] * (N + 1)
LocaOf = [None] * (N + 1)

for i, b in enumerate(B):
    for j, v in enumerate(b):
        if v is not None:
            PileOf[v] = i
            LocaOf[v] = j


def Move(v, idest):
    i = PileOf[v]
    if i == idest:
        return 99999

    j = LocaOf[v]
    hdest = HeightOf[idest]

    n = HeightOf[i] - j
    for k in range(n):
        vv = B[i][j + k]
        B[i][j + k] = None
        B[idest][hdest + k] = vv
        PileOf[vv] = idest
        LocaOf[vv] = hdest + k
    HeightOf[i] = j
    HeightOf[idest] = hdest + n

    return n + 1


def Pick(v):
    i = PileOf[v]
    j = LocaOf[v]
    if HeightOf[i] - 1 != j:
        return False

    B[i][j] = None
    PileOf[v] = 0
    LocaOf[v] = 0
    HeightOf[i] -= 1


def Heads(v):
    i = PileOf[v]
    j = LocaOf[v]
    h = HeightOf[i]

    return B[i][j + 1 : h]


cost = 0
for v in range(1, N + 1):
    i = PileOf[v]
    heads = Heads(v)
    if heads:
        idest = (i % M) + 1
        cost += Move(heads[0], idest)
        print(heads[0], idest)

    Pick(v)
    print(v, 0)
