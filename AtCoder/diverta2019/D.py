N = int(input())

s = 0
i = 1
for i in range(1,int(N**0.5)+1):
    q = N//i
    if q*i==N:
        m = q-1
        if i < m:
            s += m

print(s)

