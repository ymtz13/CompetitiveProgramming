N, K = map(int, input().split())
A = list(map(int, input().split()))

def check(l):
    k = 0
    for a in A:
        k += (a-1)//l
    return k<=K

max_ng = 0
min_ok = 10**9
while min_ok-max_ng>1:
    tgt = (min_ok+max_ng)//2
    if check(tgt):
        min_ok = tgt
    else:
        max_ng = tgt

print(min_ok)
        
