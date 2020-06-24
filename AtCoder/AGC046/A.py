X = int(input())

def gcd(a, b):
    if b>a: a,b = b,a
    while a:
        a,b = b%a, a
    return b

D = X*360//gcd(X,360)
print(D//X)
