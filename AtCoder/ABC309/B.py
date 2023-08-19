N = int(input())
A = [list(map(int, input())) for _ in range(N)]
B = [row[:] for row in A]


for n in range(1, N):
    B[0][n] = A[0][n - 1]
    B[-1][n - 1] = A[-1][n]
    B[n - 1][0] = A[n][0]
    B[n][-1] = A[n - 1][-1]

for row in B:
    print(*row, sep="")
