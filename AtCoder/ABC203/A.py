n = [0]*7
S = 0
for v in map(int, input().split()):
  n[v]+=1
  S += v

for i in range(1, 7):
  if n[i]>=2:
    print(S-i*2)
    exit()

print(0)
