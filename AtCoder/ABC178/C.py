mod = 10**9+7
N = int(input())
p = pow(10, N, mod)
q = pow( 9, N, mod)
r = pow( 8, N, mod)
print((p-q*2+r)%mod)
