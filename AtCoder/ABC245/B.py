N = int(input())
A = set(map(int, input().split()))
for ans in range(3000):
  if ans not in A: break

print(ans)
