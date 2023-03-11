R, C = map(int, input().split())
dR = abs(R - 8)
dC = abs(C - 8)

print('white' if max(dR, dC) % 2 == 0 else 'black')
