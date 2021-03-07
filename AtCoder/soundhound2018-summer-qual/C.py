n, m, d = map(int, input().split())
x = 1 if d==0 else 2
print((n-d)/(n*n)*(m-1)*x)