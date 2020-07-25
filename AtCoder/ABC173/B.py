N = int(input())
K = ['AC', 'WA', 'TLE', 'RE']
D = {k:0 for k in K}
for _ in range(N):
    D[input()]+=1

for k in K:
    print('{} x {}'.format(k, D[k]))
