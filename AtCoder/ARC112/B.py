B, C = map(int, input().split())

if B==0:
  Q, R = C//2, C%2
  ans = Q*2 if R==0 else Q*2+1
  print(ans)
  exit()

if C==1:
  print(2)
  exit()

ans = 2
if B>0:
  Q, R = C//2, C%2
  if B-Q <= 0:
    ans += 2*B-1
  else:
    ans += Q*2-1 if R==0 else Q*2

  Q, R = (C-1)//2, (C-1)%2
  ans += Q*2-1 if R==0 else Q*2
  
  print(ans)
  exit()

if B<0:
  Q, R = C//2, C%2
  ans += Q*2-1 if R==0 else Q*2

  Q, R = (C-1)//2, (C-1)%2
  if -B-Q <= 0:
    ans += 2*(-B)-1
  else:
    ans += Q*2-1 if R==0 else Q*2

  print(ans)
  exit()
