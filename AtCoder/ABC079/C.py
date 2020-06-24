from itertools import product
X = list(map(int, input()))
op = {'+':1, '-':-1}

for ops  in product(op, repeat=3):
    v = X[0] + sum([x*op[o] for x,o in zip(X[1:], ops)])
    if v==7:
        print('{X[0]}{ops[0]}{X[1]}{ops[1]}{X[2]}{ops[2]}{X[3]}=7'.format(X=X, ops=ops))
        exit()
