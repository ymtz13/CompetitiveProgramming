N = int(input())
S = [input() for _ in range(N)]
C = S.count('For')

print('Yes' if C > N // 2 else 'No')
