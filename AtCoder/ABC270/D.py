N, K = map(int, input().split())
A = list(map(int, input().split()))[::-1]

solve = [0, 1]

for n in range(2, N + 1):
  m = -1
  for a in A:
    if a > n: continue

    r = n - a
    score = a + r - solve[r]
    m = max(m, score)

  solve.append(m)

print(solve[N])
