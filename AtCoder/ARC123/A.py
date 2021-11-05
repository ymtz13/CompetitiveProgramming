A1, A2, A3 = map(int, input().split())
S = A1+A3

if S > 2*A2:
  ans = 0
  if S%2==1:
    S+=1
    ans += 1
  ans += S//2 - A2
  print(ans)

else:
  print(2*A2-S)
