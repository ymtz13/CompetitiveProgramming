N, M = map(int, input().split())
A = list(map(int, input().split()))

S = sum([a * a for a in A])

C = N - M

A.sort()
A1 = A[:C]
A2 = A[C : C * 2]

for a1, a2 in zip(A1, reversed(A2)):
    S += 2 * a1 * a2

print(S)
