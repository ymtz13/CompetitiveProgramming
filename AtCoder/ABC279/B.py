S = input()
T = input()

for i in range(len(S)):
  if S[i:i + len(T)] == T:
    print('Yes')
    exit()

print('No')
