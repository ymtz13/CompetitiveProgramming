N, H, X = map(int, input().split())
P = list(map(int, input().split()))

for i, p in enumerate(P, 1):
    if H + p >= X:
        print(i)
        exit()
