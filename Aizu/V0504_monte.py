import random
import numpy as np

def f(a,b):
    retval=1
    for i in range(b):
        retval*=(a-i)
    return retval

n, k, m, r = [int(_) for _ in input().split()]
print('n,k,m,r = ', n,k,m,r)

a=list(range(1,n+1))*k
print(a)

last_1_pos = [0]*(n*k)
min_not1 = np.zeros((n*k, n-1),int)
N=100000000
nSuc_0 = nSuc_1 = 0
for i in range(N):
    random.shuffle(a)

    for i in range(n*k):
        if a[-(i+1)]==1:
            last_1_pos[i]+=1
            if i==0 : nSuc_0 += 1
            else:
                nSuc_1 += min(a[-i:]) == a[-1]
                #min_not1[i,min(a[-i:])-2]+=1
            break

print(last_1_pos[:10])

for i in range(min(20,n*k)):
    prob_exact = k*f((n-1)*k,i) / f(n*k,i+1)
    prob_monte = last_1_pos[i]/N
    diff = prob_exact-prob_monte
    print('{:2d}  {:.6f}  {:.6f} {:+.3e}'.format(i, prob_monte, prob_exact, diff))

print(nSuc_0, nSuc_1, nSuc_0+nSuc_1)
print(nSuc_0/N, nSuc_1/N, (nSuc_0+nSuc_1)/N)
    
# print(min_not1)
# print(min_not1/np.sum(min_not1, axis=1).reshape(-1,1))
# 
# for X in range((n-1)*k):
#     prob_min_gt_m = np.array([f((n-m)*k, X)/f((n-1)*k, X) for m in range(1,n)])
#     prob_min_is_m = prob_min_gt_m.copy()
#     prob_min_is_m[:-1]-=prob_min_is_m[1:]
#     print(X,prob_min_is_m)
    
