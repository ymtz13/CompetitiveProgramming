N = int(input())
A = list(map(int, input().split()))

B = [0]
for a in A:
  B.append(a + B[-1])

C = sorted([b % 360 for b in B] + [360])

ans = 0
for i in range(len(C) - 1):
  ans = max(ans, C[i + 1] - C[i])

print(C)

print(ans)
