def check(n, b):
  while n>0:
    if n%b==7: return False
    n//=b
  return True

ans = 0
for n in range(1, int(input())+1):
  if check(n, 10) and check(n, 8): ans += 1

print(ans)