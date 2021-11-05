N = int(input())
C = input()

ans = 0

n3 = 0
coeff = 1

for i, c in enumerate(C):
  v = +1 if c == 'B' else -1 if c == 'R' else 0

  if n3 == 0:
    ans += coeff * v
    ans %= 3

  p = N - 1 - i
  q = i + 1

  if p == 0: break

  while p % 3 == 0:
    p //= 3
    n3 += 1

  while q % 3 == 0:
    q //= 3
    n3 -= 1

  coeff = coeff * p * q % 3

if N % 2 == 0: ans = -ans % 3
print('B' if ans == +1 else 'R' if ans == 2 else 'W')
