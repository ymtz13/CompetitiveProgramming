N = int(input())
A = list(map(int, input().split()))

C = [0] * N
for a in A:
  C[a] += 1

M = max(A)
if M == 1:
  print('Possible' if N == 2 else 'Impossible')
  exit()

H = M // 2
if M % 2 == 0:
  possible = min(C[H + 1:M + 1]) >= 2 and sum(C[H:M + 1]) == N and C[H] == 1
else:
  possible = min(C[H + 2:M + 1]) >= 2 and sum(
      C[H + 1:M + 1]) == N and C[H + 1] == 2

print('Possible' if possible else 'Impossible')
