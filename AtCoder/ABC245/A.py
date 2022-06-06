A, B, C, D = map(int, input().split())

X = 60 * A + B
Y = 60 * C + D
print('Takahashi' if X<=Y else 'Aoki')
