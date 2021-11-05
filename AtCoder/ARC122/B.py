N = int(input())
A = sorted(list(map(int, input().split())))
S = sum(A)
s = 0

if N==1:
  print(S/2)
  exit()

ans = S/N

for i in range(N-1):
  n = i + 1
  c = 1-2*(N-n)/N
  s += A[i]
  r = (S-s)/N

  xmin = A[i]/2
  xmax = A[i+1]/2

  ans = min(ans, xmin*c+r)
  ans = min(ans, xmax*c+r)

  #print(i)
  #print(xmin, xmin*c + r)
  #print(xmax, xmax*c + r)
  
print(ans)