N = int(input())

f = 7 / 2

for i in range(N - 1):
  f_next = 0
  for X in range(1, 7):
    f_next += max(f, X)

  f = f_next / 6

print(f)
