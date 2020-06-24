N, D, A = map(int, input().split())
XH = sorted([list(map(int, input().split())) for _ in range(N)])

bombloc = [-1]
bombdam = [ 0]
nbomb = 1
ibomb = 0 # leftmost active bomb
damage = 0
ans = 0
for x, h in XH:
    while ibomb<nbomb and bombloc[ibomb]+D<x:
        damage -= bombdam[ibomb]
        ibomb+=1
        
    h_remain = h-damage
    if h_remain<=0: continue

    n = (h_remain+A-1)//A
    bombloc.append(x+D)
    bombdam.append(n*A)
    nbomb += 1
    damage += n*A
    ans += n
    
print(ans)
