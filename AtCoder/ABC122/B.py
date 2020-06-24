S = input()
n = [0]
k=0
for c in S:
    if c in 'ACGT':
        k+=1
    elif k>0:
        n.append(k)
        k=0
if k>0: n.append(k)

print(max(n))
