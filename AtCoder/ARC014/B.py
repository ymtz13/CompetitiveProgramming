N = int(input())
w = input()
D = {w}

for i in range(N-1):
  w2 = input()
  if w2 in D or w2[0]!=w[-1]:
    print('WIN' if i%2==0 else 'LOSE')
    exit()
  D.add(w2)
  w = w2

print('DRAW')