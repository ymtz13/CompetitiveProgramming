N = int(input())
Q = [tuple(map(int, input().split())) for _ in range(N)]


Q.sort(key=lambda x:x[0])
Lmax_2nd = Q[-2][0]
Q.sort(key=lambda x:x[1])
Rmin_2nd = Q[1][1]
length = [r-l+1 for l,r in Q]
#print(Q)

Q_Lmax = max(Q, key=lambda x:x[0])
Lmax = Q_Lmax[0]
Q_Rmin = min(Q, key=lambda x:x[1])
Rmin = Q_Rmin[1]

if Q_Lmax[1]==Rmin: # single Question have maxL & minR
    print(Rmin-Lmax+1 + max(length))
    exit()

Q_lorder = sorted(Q, key=lambda x: x[0]-x[1])
iQ_longest = 0
if Q_lorder[iQ_longest]==Q_Lmax and Lmax_2nd < Lmax: iQ_longest += 1
Q_longest = Q_lorder[iQ_longest]
xx = Rmin
if Q_longest[1]==Rmin: xx = Rmin_2nd
ans = max(Rmin_2nd-Lmax+1, 0) + Q_longest[1]-Q_longest[0]+1

#print(Q_longest, Rmin, Lmax)
#print(ans)

#print('LM' , Q_Lmax)
#print('RM' , Q_Rmin)

Lmax_g2 = Q_Rmin[0]
i = 0
Rd = Rmin#+1
gk = 10**10
Q.append((0,gk))
while Rd<gk:
    print(i,Rd, Q[i][1])
    while Q[i][1]<=Rd: i+=1
    Rd = Q[i][1]
    Lmax_g2 = max(Lmax_g2, Q[i-1][0])
    print(Rd, Rmin, Lmax_g2, max(Rmin-Lmax_g2+1, 0) ,  max(min(Rd, Q_Lmax[1])-Lmax+1, 0))
    ans = max(ans, max(Rmin-Lmax_g2+1, 0) + max(min(Rd, Q_Lmax[1])-Lmax+1, 0))

print(ans)
