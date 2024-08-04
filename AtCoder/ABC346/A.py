N = int(input())
A = list(map(int, input().split()))
B = [a0 * a1 for a0, a1 in zip(A, A[1:])]
print(*B)
