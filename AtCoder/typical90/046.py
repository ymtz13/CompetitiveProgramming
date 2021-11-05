N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
Da = [0]*46
Db = [0]*46
Dc = [0]*46
for a, b, c in zip(A, B, C):
  Da[a%46] += 1
  Db[b%46] += 1
  Dc[c%46] += 1

ans = 0
for a in range(46):
  for b in range(46):
    c = (-a-b)%46
    ans += Da[a]*Db[b]*Dc[c]

print(ans)
