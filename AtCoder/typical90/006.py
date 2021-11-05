N, K = map(int, input().split())
S = input()

C = [0]*26
ans = []

for i, c in enumerate(S):
  c = ord(c)-ord('a')
  C[c] += 1
  for j in range(c+1, 26): C[j] = 0

  if N-i<=K:
    for j, count in enumerate(C):
      if count > 0:
        ans.append(j + ord('a'))
        C[j] -= 1
        break
  
print(''.join(map(chr, ans)))
