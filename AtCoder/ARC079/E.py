N = int(input())
A = list(map(int, input().split()))

def check_x(x):
    s = 0
    for a in A:
        b = a+x
        s += b//(N+1) + (b%(N+1))//N
    return s<=x

def check(z):
    ok = False
    for x in range(z, max(-1, z-N), -1):
        ok = ok or check_x(x)
    return ok

min_ok = 10**20
max_ng = -1

while min_ok-max_ng>1:
    tgt = (min_ok+max_ng)//2
    if check(tgt):
        min_ok = tgt
    else:
        max_ng = tgt

print(min_ok)
