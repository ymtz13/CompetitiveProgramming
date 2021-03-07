N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
mA = 0
mAB = 0
for a, b in zip(A, B):
  mA = max(mA, a)
  mAB = max(mAB, mA * b)
  print(mAB)
