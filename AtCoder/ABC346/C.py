N, K = map(int, input().split())
A = list(map(int, input().split()))
S = {a for a in A if a <= K}

print(K * (K + 1) // 2 - sum(S))
