K = int(input())

def gcd(x, y):
    if x>y: x,y=y,x
    while x: x,y = y%x,x
    return y

