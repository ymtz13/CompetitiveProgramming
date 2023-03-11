N, L = map(int, input().split())
A = list(map(int, input().split()))

for a in A:
  if L > a:
    L -= a + 1

  elif L == a:
    L = 0

  elif a == 2:
    print('No')
    exit()

print('Yes')
