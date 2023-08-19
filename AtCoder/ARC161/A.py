from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
D = defaultdict(int)

M = N // 2 + 1

if N == 1:
    print("Yes")
    exit()

for a in A:
    D[a] += 1

A.sort()
a = A[M]

print("Yes" if D[a] < M else "No")
