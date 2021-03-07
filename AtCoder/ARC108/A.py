S, P = map(int, input().split())
ans = 'No'
for N in range(1, 1000001):
  M = S - N
  if M>0 and N*M==P:
    ans = 'Yes'
    break
print(ans)