input()
H = [int(c) for c in input().split()]
nvisible=0
for i,hi in enumerate(H):
    visible=1
    for hj in H[:i]:
        if hj>hi:
            visible=0
            break
    nvisible+=visible
print(nvisible)
