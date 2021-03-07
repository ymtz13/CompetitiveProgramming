N = int(input())
X = [0]*10001
for _ in range(N): X[int(input())] += 1

p = 1
mod = 10**9+7
f = [1]*10001
for i in range(1, 10001):
  f[i] = p = p * i % mod

s = u = 0
z = 1
for t, x in enumerate(X):
  for i in range(x):
    s += t
    u += s
  z = z * f[x] % mod

print(u)
print(z)
