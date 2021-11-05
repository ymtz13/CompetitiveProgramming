from collections import defaultdict

N = int(input())

if N==1:
  print(1)
  print(1)
  exit()

def solve(n):
  count = 0
  x = 1
  y = 0
  while 2*x+y<=n:
    y += x
    x += y
    count += 1
  
  return x, n-x, count

counts = defaultdict(int)
while N:
  _, N, count = solve(N)
  #print(_, N, count)
  counts[count] += 1

C = max(counts.keys())
#print(counts, C)

x = y = 0
actions = []

for i in range(C, -1, -1):
  for cc in range(counts[i]):
    actions.append(1)
    x+= 1

  if i==0: break
    
  actions.append(4)
  y+=x
  actions.append(3)
  x+=y
  

#print('debug:', x, y)

print(len(actions))
for a in actions:
  print(a)
