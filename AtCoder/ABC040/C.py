N = int(input())
A = list(map(int, input().split()))
C = [0] * N
C[1] = abs(A[0]-A[1])
for i in range(2, N):
    C[i] = min(abs(A[i-1]-A[i]) + C[i-1], abs(A[i-2]-A[i]) + C[i-2])
print(C[-1])
