N = int(input())
M = 1000000
A = [0]*(M+10)
for _ in range(N): A[int(input())] += 1
S = [0]*(M+10)
s = N
for i, a in enumerate(A):
  S[i] = s
  s -= A[i]

S[0] = S[1]

def border(k):
  min_ok = M+5
  max_ng = -1
  while min_ok-max_ng>1:
    tgt = (min_ok + max_ng)//2
    if S[tgt]<=k:
      min_ok = tgt
    else:
      max_ng = tgt

  return min_ok


for _ in range(int(input())):
  print(border(int(input())))
