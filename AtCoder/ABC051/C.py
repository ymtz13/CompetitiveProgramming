sx, sy, tx, ty = list(map(int, input().split()))
x = tx-sx
y = ty-sy

print('D', 'R'*(x+1), 'U'*(y+1), 'L', sep='', end='')
print('D'*y, 'L'*x, sep='', end='')
print('L', 'U'*(y+1), 'R'*(x+1), 'D', sep='', end='')
print('L'*x, 'D'*y, sep='')




#  
#     T+
#     ||
#  S--+|
#  +---+
