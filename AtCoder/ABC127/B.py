r, D, x = [int(c) for c in input().split()]

for i in range(10):
    x = r*x - D
    print(x)
