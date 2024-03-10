N = int(input())
A = list(map(int, input().split()))
for i in range(N - 1):
    S, T = map(int, input().split())
    n = A[i] // S
    A[i + 1] += n * T

print(A[-1])
