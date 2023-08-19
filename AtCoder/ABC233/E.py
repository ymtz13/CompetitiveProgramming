X = list(map(int, input()))
N = len(X)

C = []
c = [0] * 10
for x in X:
  c[x] += 1
  C.append(c[:])

ans = []
carry = 0
for c in reversed(C):
  s = carry
  for i, v in enumerate(c):
    s += i * v
  ans.append(s % 10)
  carry = s // 10

if carry:
  ans.append(carry)

print(''.join(map(str, ans[::-1])))
