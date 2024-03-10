X = int(input())
N = int(input())

for n in range(1, 100000000000):
    r = X % 3
    if r == 0:
        X += 1
    if r == 1:
        X *= 2
    if r == 2:
        X *= 3

    if X >= N:
        print(n)
        break
