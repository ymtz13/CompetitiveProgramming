N = int(input())
A = sorted([int(c)-i-1 for i, c in enumerate(input().split())])
b = A[N//2]
ans = sum([abs(a-b) for a in A])
print(ans)

