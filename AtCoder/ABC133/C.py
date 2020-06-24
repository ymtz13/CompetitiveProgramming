L, R = [int(c) for c in input().split()]

if R-L+1 >= 2019:
    print(0)
    exit()

m = 2020
l = [c%2019 for c in range(L,R+1)]
for i in range(len(l)):
    for j in range(i+1, len(l)):
        m = min(m, (l[i]*l[j])% 2019)
            
print(m)
