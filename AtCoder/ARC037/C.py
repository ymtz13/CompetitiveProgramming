N, K = map(int, input().split())
A = sorted(list(map(int, input().split())), reverse=True)
B = sorted(list(map(int, input().split())))


def check(X):
  n = 0
  i = 0
  for a in A:
    while i<N and a*B[i]<=X: i+=1
    n+=i
  
  return n>=K

min_ok = 10**20
max_ng = 0
while min_ok-max_ng>1:
  tgt = (min_ok+max_ng)//2
  if check(tgt):
    min_ok = tgt
  else:
    max_ng = tgt

print(min_ok)
