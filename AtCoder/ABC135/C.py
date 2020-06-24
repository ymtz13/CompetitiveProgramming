N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
D = 0
for i in range(N):
    d = min(A[i], B[i])
    D += d
    A[i] -= d
    B[i] -= d

    d = min(A[i+1], B[i])
    D += d
    A[i+1] -= d

print(D)
