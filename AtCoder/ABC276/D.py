N = int(input())
A = list(map(int, input().split()))

F2 = []
F3 = []
F = []

for a in A:
  f2 = 0
  while a % 2 == 0:
    f2 += 1
    a //= 2

  f3 = 0
  while a % 3 == 0:
    f3 += 1
    a //= 3

  F2.append(f2)
  F3.append(f3)
  F.append(a)

if len(set(F)) > 1:
  print(-1)
  exit()

n2 = sum(F2) - min(F2) * N
n3 = sum(F3) - min(F3) * N

print(n2 + n3)
