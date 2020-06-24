S = input()

nx = 0
for c in S:
    if c=='x': nx+=1

if nx<=7:
    print('YES')
else:
    print('NO')
