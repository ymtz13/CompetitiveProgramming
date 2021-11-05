N, K = map(int, input().split())
A = sorted(list(map(int, input().split())), reverse=True) + [0]

p = A[0]
n = 1
k = K
ans = 0
for a in A[1:]:
  diff = p - a

  if diff * n <= k:
    ans += n * (p * (p + 1) // 2 - a * (a + 1) // 2)
    p = a
    k -= diff * n
    n += 1
    #print(diff, n, k, ans)

  else:
    q = k // n
    r = k % n

    a = max(0, p - q)
    ans += n * (p * (p + 1) // 2 - a * (a + 1) // 2)
    #print(q, r, k, a, ans)
    ans += a * r
    break

print(ans)