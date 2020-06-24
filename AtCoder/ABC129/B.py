N = int(input())
W = [int(c) for c in input().split()]

min_diff = sum(W)
for i in range(1,N):
    min_diff = min(abs(sum(W[:i])-sum(W[i:])), min_diff)

print(min_diff)
