r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

def ans(value):
  print(value)
  exit()

if r1==r2 and c1==c2: ans(0)

if r1+c1 == r2+c2: ans(1)
if r1-c1 == r2-c2: ans(1)
if abs(r1-r2)+abs(c1-c2) <= 3: ans(1)

rp = r1 + c1 - c2
rn = r1 - c1 + c2
if abs(rp-r2) <= 3: ans(2)
if abs(rn-r2) <= 3: ans(2)
if abs(r1-r2)+abs(c1-c2) <= 6: ans(2)
if (r1+c1)%2 == (r2+c2)%2: ans(2)

ans(3)