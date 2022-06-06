N = int(input())
X = 1 << 31
print('Yes' if -X <= N < X else 'No')
