N = int(input())
A = list(map(int, input().split()))

mod = 1000000007

c = [0,0,0]
ans = 1
for a in A:
    ans *= c.count(a)%mod
    for i in range(3):
        if c[i]==a:
            c[i]+=1
            break

print(ans%mod)


    
