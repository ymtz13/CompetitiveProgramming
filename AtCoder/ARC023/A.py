y = int(input())
m = int(input())
d = int(input())
if m <= 2:
  y -= 1
  m += 12

def f(y, m, d):
  return 365*y + y//4 - y//100 + y//400 + 306*(m+1)//10 + d - 429

print(f(2014, 5, 17) - f(y, m, d))