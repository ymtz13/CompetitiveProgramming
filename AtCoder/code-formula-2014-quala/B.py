input()
X = ['x']*10
for p in input().split(): X[int(p)] = '.'
for q in input().split(): X[int(q)] = 'o'

print("""{0[7]} {0[8]} {0[9]} {0[0]}
 {0[4]} {0[5]} {0[6]}
  {0[2]} {0[3]}
   {0[1]}""".format(X))
