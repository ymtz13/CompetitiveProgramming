N = int(input())

for k in range(N+3):
  if k*(k-1)//2 == N: break

if k==N+2:
  print('No')
  exit()

print('Yes')
print(k)
S = [[] for _ in range(k)]
c = 1
for i in range(k):
  for j in range(i+1, k):
    S[i].append(c)
    S[j].append(c)
    c += 1

for s in S:
  print(len(s), ' '.join(map(str, s)))
