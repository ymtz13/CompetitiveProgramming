N = int(input())
A = list(map(int, input().split()))

minA = min(A)
maxA = max(A)
S = sum(range(minA, maxA + 1))

print(S - sum(A))
