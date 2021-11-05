from collections import defaultdict

N = int(input())
D = defaultdict(int)

for _ in range(N):
  A, B = map(int, input().split())
  D[A] += 1
  D[A + B] -= 1

D[1 << 60] = 0

E = sorted(D.items())

ans = [0] * (N + 1)
s = 0
p = 0
for day, diff in E:
  ans[s] += day - p
  s += diff
  p = day

print(' '.join(map(str, ans[1:])))
