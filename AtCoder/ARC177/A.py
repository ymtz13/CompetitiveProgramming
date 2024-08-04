A = list(map(int, input().split()))
A.reverse()
D = [500, 100, 50, 10, 5, 1]

N = int(input())
X = list(map(int, input().split()))

for x in X:
    for i in range(6):
        d = D[i]
        y = x // d
        n = min(y, A[i])
        x -= n * d
        A[i] -= n

    if x > 0:
        print("No")
        exit()

print("Yes")
