T = int(input())
for _ in range(T):
  ax, ay, bx, by, cx, cy = map(int, input().split())

  gx = ax if ax==bx or ax==cx else bx
  gy = ay if ay==by or ay==cy else by

  dx = +1 if gx*3 < ax+bx+cx else -1
  dy = +1 if gy*3 < ay+by+cy else -1

  ans = 0

  # 蟹歩き
  if dx*dy<0:
    d = max(0, min(abs(dx), abs(dy))-1)
    ans += d*2
    if dx<0:
      dx += d
      dy -= d
    else:
      dx -= d
      dy += d
    


  # 
  