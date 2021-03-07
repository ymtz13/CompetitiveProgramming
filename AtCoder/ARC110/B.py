input()
T = input()
N = len(T)
R = 10**10

def pans(v):
  print(v)
  exit()

if T == '0': pans(R)
if T == '1': pans(R*2)
if T == '00': pans(0)
if T == '01': pans(R-1)
if T == '10': pans(R)
if T == '11': pans(R)

s = 0
if T[:1] ==  '0' : s = 1
if T[:2] == '10' : s = 2

n = 0
for i in range(s, N-2, 3):
  if T[i:i+3] != '110': pans(0)
  n += 1

ans = R - n + 1
if s > 0: ans -= 1

if (N-s)%3 == 1:
  if T[-1:] != '1' : pans(0)
  ans -= 1

if (N-s)%3 == 2:
  if T[-2:] != '11': pans(0)
  ans -= 1

print(ans)
