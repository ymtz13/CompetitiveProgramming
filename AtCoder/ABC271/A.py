C = '0123456789ABCDEF'

N = int(input())
v0 = N // 16
v1 = N % 16

ans = C[v0] + C[v1]
print(ans)
