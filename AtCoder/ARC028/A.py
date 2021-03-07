N, A, B = map(int, input().split())
R = N%(A+B)
print('Ant' if 1<=R and R<=A else 'Bug')
