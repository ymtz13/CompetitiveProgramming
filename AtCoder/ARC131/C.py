N = int(input())
A = list(map(int, input().split()))

S = 0
for a in A:
  S ^= a

if S in A:
  print('Win')
  exit()

print('Win' if N % 2 == 1 else 'Lose')
