B = [list(input()) for _ in range(19)]

def judge(s):
  for r in range(19):
    streak = 0
    for c in range(19):
      streak = streak + 1 if B[r][c] == s else 0
      if streak>=5: return True

  for c in range(19):
    streak = 0
    for r in range(19):
      streak = streak + 1 if B[r][c] == s else 0
      if streak>=5: return True
  
  for i in range(19):
    streak = 0
    for j in range(i+1):
      streak = streak + 1 if B[j][i-j] == s else 0
      if streak>=5: return True
  
  for i in range(19):
    streak = 0
    for j in range(i, 19):
      streak = streak + 1 if B[j][18+i-j] == s else 0
      if streak>=5: return True
  
  for i in range(19):
    streak = 0
    for j in range(19-i):
      streak = streak + 1 if B[j][i+j] == s else 0
      if streak>=5: return True

  for i in range(19):
    streak = 0
    for j in range(i, 19):
      streak = streak + 1 if B[j][j-i] == s else 0
      if streak>=5: return True

  return False

nB = sum([b.count('o') for b in B])
nW = sum([b.count('x') for b in B])
diff = nB-nW
if diff>1 or diff<0:
  print('NO')
  exit()

winB = judge('o')
winW = judge('x')

if winB and winW:
  print('NO')
  exit()

if (not winB) and (not winW):
  print('YES')
  exit()

if (winB and diff!=1) or (winW and diff!=0):
  print('NO')
  exit()

t = 'o' if winB else 'x'
for r in range(19):
  for c in range(19):
    if B[r][c]!=t: continue
    B[r][c]='.'
    if not judge(t):
      print('YES')
      exit()
    B[r][c]=t

print('NO')