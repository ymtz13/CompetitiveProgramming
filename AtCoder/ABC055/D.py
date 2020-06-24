N = int(input())
S = input()

a = {'S':'W', 'W':'S'}
for t0, t1 in ('SS', 'SW', 'WS', 'WW'):
    T = [t0, t1]
    for i in range(2, N+2):
        if (S[(i-1)%N]=='o' and T[-1]=='S') or (S[(i-1)%N]=='x' and T[-1]=='W'):
            T.append(T[-2])
        else:
            T.append(a[T[-2]])

    if T[0]==T[-2] and T[1]==T[-1]:
        print(''.join(T[:-2]))
        exit()
print(-1)
