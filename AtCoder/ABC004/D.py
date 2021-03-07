R, G, B = map(int, input().split())

def solve(x, y):
  retval = x*(x+1)//2 + (y-1)*y//2
  if x>=100: retval += (x-99)*y
  return retval

print(solve(G//2, min(R, B)) + solve((G-1)//2, max(R, B)))