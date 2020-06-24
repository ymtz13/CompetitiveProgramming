N = int(input())
a = [int(input()) for _ in range(N)]

b = [0]*(max(a)+1)
for x in a:
    b[x]+=1

for i in enumerate(b):
    print(i)


nn = [0]
for i in range(sum(a)+1):
    s=b[i]
    for k in range(i):
        s+=nn[k]*b[i-k]
    nn.append(s)

print(nn)
