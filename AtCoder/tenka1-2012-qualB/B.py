import string

def ans(c):
  print(c)
  exit()

S0 = input()

ns = ne = 0
for c in S0:
  if c != '_': break
  ns += 1

for c in S0[::-1]:
  if c != '_': break
  ne += 1

if ns == len(S0): ans(S0)

S = S0[ns:len(S0)-ne]

isSnake = True
camel = ''
for i, w in enumerate(S.split('_')):
  if len(w) == 0 or w[0] not in string.ascii_lowercase: isSnake = False
  for c in w[1:]:
    if c in string.ascii_uppercase: isSnake = False
  
  if isSnake:
    camel += w[0].upper() + w[1:] if i>0 else w

if isSnake: ans('_'*ns + camel + '_'*ne)


if S[0] not in string.ascii_lowercase or '_' in S: ans(S0)

snake = ''
w = ''
for c in S:
  if c in string.ascii_uppercase:
    snake += w.lower() + '_'
    w = ''
  w += c
snake += w.lower()

ans('_'*ns + snake + '_'*ne)