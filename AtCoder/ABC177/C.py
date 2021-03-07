N = int(input())
A = list(map(int, input().split()))

mod = 10**9+7

S = 0
T = 0
for a in A:
    S = (S+a  )%mod
    T = (T+a*a)%mod

ans = (S*S-T)%mod
print(ans*pow(2, mod-2, mod)%mod)
