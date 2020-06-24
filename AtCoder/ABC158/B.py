N, A, B = map(int, input().split())
p = N//(A+B)
r = N%(A+B)
print(p*A+min(r,A))
