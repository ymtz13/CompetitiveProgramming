N = int(input())
C = [int(input()) for _ in range(N)]

n0 = C.count(0)
if n0==0 or n0==N:
  print(-1)
  exit()

C = C*2
streak = m = 0
p = None
for c in C:
  if c!=p:
    m = max(m, streak)
    streak = 0
  streak += 1
  p = c

print((m+1)//2)
