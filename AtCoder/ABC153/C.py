N, K = list(map(int, input().split()))
S = sum(sorted(list(map(int, input().split())), reverse=True)[K:])
print(S)
