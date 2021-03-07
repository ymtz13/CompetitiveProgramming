S = input()
n = 5
combo = 0
charge = 0
ans = 0
queue = [0]*10
queue_dmg = [0]*10

for t, c in enumerate(S):
  n += queue[t%10]
  combo += queue_dmg[t%10]
  queue[t%10] = 0
  queue_dmg[t%10] = 0
  if charge > 0:
    charge += 1
    if charge > 2:
      queue[(t+7)%10] += 3
      queue_dmg[(t+2)%10] += 1
      charge = 0

  elif c=='N':
    if n > 0:
      n -= 1
      ans += 10 + combo//10
      queue[(t+7)%10] += 1
      queue_dmg[(t+2)%10] += 1
  
  elif c=='C':
    if n > 2:
      n -= 3
      charge = 1
      ans += 5 * (10 + combo//10)
  
print(ans)
