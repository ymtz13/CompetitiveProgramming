N, R = map(int, input().split())
S = ' ' + input()
x = N
P = []
while x>0:
  if S[x] == '.':
    P.append(x-R+1)
    x = x-R+1
  x -= 1

p = max(1, P[0]) if P else 0
assert R<=N
print(p - 1 + len(P) if P else 0)
