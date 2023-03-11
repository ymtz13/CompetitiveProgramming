X = int(input())

B = [1 << i for i in range(70) if (1 << i) & X]

N = len(B)
for q in range(1 << N):
  s = 0
  for j, b in enumerate(B):
    if q & (1 << j): s += b

  print(s)
