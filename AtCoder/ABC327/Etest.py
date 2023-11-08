from math import sqrt

for k in range(1, 5001):
    print(k**0.5, sqrt(k))
exit()

N = 500
r = 0.9

d = 0
for k in range(1, N+1):
    d = d*r+1
    d0 = (1-r**k) / (1-r)
    print(k, (d-d0)/d0, d0, d)


#      d = 1 + r + ... + r^(N-1)
#     rd =     r + ... + r^(N-1) + r^N
# (1-r)d = 1 -                     r^N 

#d0 = (1-0.9**N)/(1-0.9)

