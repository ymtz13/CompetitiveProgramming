A, B, K = list(map(int, input().split()))
k = min(A, K)
print(A-k, max(0,B-(K-k)))
