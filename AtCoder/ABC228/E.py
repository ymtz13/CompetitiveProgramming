N, K, M = map(int, input().split())
mod = 998244353
#mod = 7

def solve(N, K, M):
  if M % mod == 0: return 0

  X = pow(K, N, mod - 1)
  ans = pow(M, X, mod)
  return ans


def solve2(N, K, M):
  X = pow(K, N)
  ans = pow(M, X, mod)
  return ans


def solve3(N, K, M):
  X = pow(K, N)
  ans = pow(M, X)
  return ans % mod


print(solve(N, K, M))

exit()
print(solve2(N, K, M))
print(solve3(N, K, M))

for N in range(1, 20):
  for K in range(1, 20):
    for M in range(1, 10):
      s1 = solve(N, K, M)
      s2 = solve2(N, K, M)
      s3 = solve3(N, K, M)
      assert s1 == s2 and s2 == s3
      print(N, K, M)
