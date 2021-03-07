N = int(input())
ans = 1
for i in range(N):
  S = input()
  if S=='OR': ans += pow(2, i+1)

print(ans)
 