N = int(input())
A = map(int, input().split())
B = map(int, input().split())
S = 0
for a, b in zip(A, B):
  S += a*b

print('Yes' if S==0 else 'No')
