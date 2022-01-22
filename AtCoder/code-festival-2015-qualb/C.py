N, M = map(int, input().split())
A = sorted(list(map(int, input().split()))) + [1 << 60]
B = sorted(list(map(int, input().split())))

i = 0
for b in B:
  while A[i] < b:
    i += 1

  if i == N:
    print('NO')
    exit()

  i += 1

print('YES')
