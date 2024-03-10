N = int(input())
A = list(map(int, input().split()))
M = max(A)
B = [a for a in A if a < M]
print(max(B))
