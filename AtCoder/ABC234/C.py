K = int(input())

ans = []
for i in range(100, -1, -1):
  b = 1 << i
  if K&b:
    ans.append('2')
  elif len(ans):
    ans.append('0')

print(''.join(ans))
