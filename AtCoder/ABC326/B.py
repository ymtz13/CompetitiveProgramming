N = int(input())

for n in range(N, 1000):
    n0 = n // 100
    n1 = (n % 100) // 10
    n2 = n % 10

    if n0 * n1 == n2:
        print(n)
        exit()
