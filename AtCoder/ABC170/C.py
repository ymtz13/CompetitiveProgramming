X, N = map(int, input().split())
P = set(map(int, input().split()))
d = 0
while True:
    x = X-d
    if x not in P: break

    x = X+d
    if x not in P: break

    d += 1

print(x)
