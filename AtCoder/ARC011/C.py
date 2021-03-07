first, last = input().split()
N = int(input())
S = [first, last] + [input() for _ in range(N)]
E = [[] for _ in range(N+2)]

def diff(w1, w2):
  d = 0
  for c1, c2 in zip(w1, w2):
    if c1!=c2: d+=1
  return d

if diff(first, last)<2:
  print(0)
  print(first)
  print(last)
  exit()

for i, wi in enumerate(S):
  for j, wj in enumerate(S[:i]):
    if diff(wi, wj)==1:
      E[i].append(j)
      E[j].append(i)

queue = [(0, 0, -1)]
iq = 0
dist = [-1]*(N+2)
parent = [None]*(N+2)
while iq < len(queue):
  q, d, p = queue[iq]
  iq += 1

  if dist[q]>=0: continue
  dist[q] = d
  parent[q] = p

  queue += [(e, d+1, q) for e in E[q]]

if parent[1] is None:
  print(-1)
  exit()

ans = [1]
while ans[-1]>0: ans.append(parent[ans[-1]])

print(len(ans)-2)
for a in ans[::-1]:
  print(S[a])
