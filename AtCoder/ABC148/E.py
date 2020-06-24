N = int(input())
if N%2==1:
    print(0)
    exit()

k = 1
ans = 0
while True:
    n = N//(2*(5**k))
    if n==0: break
    ans += n
    k +=1
print(ans)
