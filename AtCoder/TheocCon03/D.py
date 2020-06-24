N = int(input())
s = input()

S,W = 0,1 # 0->sheep,  1->wolf
start = [[S,S], [S,W], [W,S], [W,W]] 
for animals in start:
    for i in range(2, N):
        if s[i-1]=='o': animals.append(  animals[i-2])
        else:           animals.append(1-animals[i-2])
        if animals[i-1]==W:
            animals[i] = 1-animals[i]

    if animals[0]==S and ((s[0]=='o' and  animals[-1]==animals[1]) or
                          (s[0]=='x' and  animals[-1]!=animals[1])):
            print(''.join(['SW'[x] for x in animals]))
            exit()

    if animals[0]==W and ((s[0]=='o' and  animals[-1]!=animals[1]) or
                          (s[0]=='x' and  animals[-1]==animals[1])):
            print(''.join(['SW'[x] for x in animals]))
            exit()

print(-1)
