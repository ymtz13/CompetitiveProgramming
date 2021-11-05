N, X = map(int, input().split())
A = list(map(int, input().split()))
S = sum(A) - N//2
print('Yes' if X>=S else 'No')
