def comb(n, k):
  retval = 1
  for i in range(k):
    retval *= (n-i)
    retval //= (1+i)
  return retval

L = int(input())
print(comb(L-1, 11))