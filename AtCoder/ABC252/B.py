_ = input()
A = list(map(int, input().split()))
B = set(map(int, input().split()))

M = max(A)
S = {i + 1 for i, a in enumerate(A) if a == M}

print('Yes' if B & S else 'No')
