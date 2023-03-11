N = int(input())
A = list(map(int, input().split()))

B = [a for a in A if a >= N]

if len(B) == 0:
  ans = 'Bob'

if len(B) == 1:
  ans = 'Alice'

if len(B) >= 2:
  if B[-2] + 1 == B[-1] and (B[-1] - N) % 2 == 1:
    ans = 'Bob'
  else:
    ans = 'Alice'

print(ans)
