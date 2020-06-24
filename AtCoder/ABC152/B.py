a, b = input().split()
x = a*int(b)
y = b*int(a)
print(x if x<y else y)
