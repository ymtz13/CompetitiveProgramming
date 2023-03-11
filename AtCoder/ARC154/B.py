oa = ord('a')

N = int(input())
S = input()
T = input()

if sorted(S) != sorted(T):
  print(-1)
  exit()

m = 0
Sinv = S[::-1]
for t in T[::-1]:
  if t == Sinv[m]:
    m += 1

print(N - m)
