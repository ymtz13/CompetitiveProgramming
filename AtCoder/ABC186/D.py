N = int(input())
A = sorted(list(map(int, input().split())), reverse=True)
s = ans = 0
for i, a in enumerate(A):
  ans += s - a*i
  s += a
print(ans)