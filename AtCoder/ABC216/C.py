N = int(input())

B = bin(N)[2:]
ans = []
test = 0
for b in B:
  if b=='1':
    ans.append('A')
    test += 1
  ans.append('B')
  test *= 2

print(''.join(ans[:-1]))
