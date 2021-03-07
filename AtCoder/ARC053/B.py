S = input()
N = [0]*26
for c in S: N[ord(c)-ord('a')]+=1

p = 0
q = 0
for n in N:
    p += n%2
    q += n//2

if p==0:
    print(q*2)
else:
    print(1+q//p*2)
    
