N = int(input())
S = input()
if S[0]!=S[-1]:
  print(1)
  exit()

x = S[0]

for i in range(N-1):
  if S[i]!=x and S[i+1]!=x:
    print(2)
    exit()

print(-1)
