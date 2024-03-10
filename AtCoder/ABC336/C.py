N = int(input()) - 1

if N == 0:
    print(0)
    exit()

X = []
while N:
    X.append((N % 5) * 2)
    N //= 5

print(*X[::-1], sep="")
