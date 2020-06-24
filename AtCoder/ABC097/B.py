X = int(input())
ans = 1
a = 2
while a*a<=X:
    r = a*a
    while r<=X:
        ans = max(ans, r)
        r*=a
    a+=1

print(ans)
