def ans(b):
  print('Yes' if b else 'No')
  exit()


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

nodd = 0

for a, b in zip(A, B):
  if a % 2 == 1: nodd += 1

if sorted(A) != sorted(B):
  ans(False)

if nodd == 0:
  ans(True)

if nodd == N:
  ans(A == B)


def oddPair(A):
  o = []
  for v in A:
    if v % 2 == 1: o.append(v)

  return len(o) == 2


PA = False
PB = False
for i in range(N - 2):
  if oddPair(A[i:i + 3]): PA = True
  if oddPair(B[i:i + 3]): PB = True
  print(A[i:i + 3], oddPair())

if PA and PB:
  ans(True)

if PA or PB:
  ans(False)

xA = []
xB = []

XA = []
XB = []

for a, b in zip(A, B):
  if a % 2 == 1 and a != b: ans(False)
  if b % 2 == 1 and a != b: ans(False)

  if a % 2 == 1:
    XA.append(xA)
    XB.append(xB)
    xA = []
    xB = []

  else:
    xA.append(a)
    xB.append(b)

XA.append(xA)
XB.append(xB)

for xA, xB in zip(XA, XB):
  if len(xA) == 2:
    if xA != xB:
      ans(False)

  else:
    if sorted(xA) != sorted(xB):
      ans(False)

ans(True)
