T = int(input())

ans = []
for _ in range(T):
  L, R = input().split()

  if len(L) == len(R):
    ans.append(int(R) - int(L) + 1)

  else:
    X = int(R) - 10**(len(R) - 1) + 1

    if int(R[0]) > 1:
      ans.append(X)

    else:
      M = max(int(R[1:]), int(R[:-1]), int(L) - 1)
      ans.append(int(R) - M)
      # if int(R[1]) > 0:

      # else:
      #   ans.append(int(R) - int(R[:-1]))

for a in ans:
  print(a)
