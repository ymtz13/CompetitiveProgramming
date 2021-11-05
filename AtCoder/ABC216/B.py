N = int(input())
S = {input() for _ in range(N)}
print('Yes' if len(S) < N else 'No')
