S = input()

T = [0]
i = 0
while i < len(S) - 1:
  if S[i:i + 2] == '25':
    T[-1] += 1
    i += 2
  else:
    if T[-1] > 0: T.append(0)
    i += 1

ans = 0
for t in T:
  ans += t * (t + 1) // 2

print(ans)
