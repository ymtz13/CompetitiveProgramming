N = int(input())
A = list(map(int, input().split()))

S = 0
for a in A:
  S = S * 2 + a

print(S)
