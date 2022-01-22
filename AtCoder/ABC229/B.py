A, B = input().split()
A = A[::-1] + '0' * 20
B = B[::-1] + '0' * 20

ans = 'Easy'
for a, b in zip(A, B):
  if int(a) + int(b) >= 10: ans = 'Hard'
print(ans)
