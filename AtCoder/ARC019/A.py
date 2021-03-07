S = input()
def f(c):
  if c=='O': return '0'
  if c=='D': return '0'
  if c=='I': return '1'
  if c=='Z': return '2'
  if c=='S': return '5'
  if c=='B': return '8'
  return c

print(''.join(map(f, S)))
