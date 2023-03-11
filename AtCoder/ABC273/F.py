N, X = map(int, input().split())
Y = [(i, y) for i, y in enumerate(map(int, input().split()))]
Z = [(i, z) for i, z in enumerate(map(int, input().split()))]

sY = sorted(Y, key=lambda x: x[1])
sZ = sorted(Z, key=lambda x: x[1])


