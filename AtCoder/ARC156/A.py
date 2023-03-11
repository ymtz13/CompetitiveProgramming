T = int(input())
Ans = []

for _ in range(T):
  N = int(input())
  S = input()

  cnt = S.count('1')
  if cnt & 1:
    Ans.append(-1)
    continue

  if cnt != 2:
    Ans.append(cnt // 2)

  elif '11' not in S:
    Ans.append(1)

  elif N <= 3:
    Ans.append(-1)

  elif S == '0110':
    Ans.append(3)

  else:
    Ans.append(2)

for a in Ans:
  print(a)
