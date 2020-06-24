
def parse(expr):
    if expr=='' : return None
    
    depth=0
    for i, c in enumerate(expr):
        if c=='(': depth+=1
        if c==')': depth-=1
        if c==',' and depth==1: break

    return [parse(expr[1:i]), parse(expr[i+1:-1])]

def encode(tree):
    if tree==None: return ''
    return '(' + encode(tree[0]) + ',' + encode(tree[1]) + ')'

def intersection(tree1, tree2):
    if tree1 == None or tree2==None : return None
    return [intersection(tree1[0], tree2[0]), intersection(tree1[1], tree2[1])]

def union(tree1, tree2):
    if tree1 == None and tree2==None : return None
    if tree1 == None : tree1 = [None, None]
    if tree2 == None : tree2 = [None, None]
        
    return [union(tree1[0], tree2[0]), union(tree1[1], tree2[1])]


while True:
    try:
        method, expr1, expr2 = input().split()
        if method=='i':
            tree =  intersection(parse(expr1), parse(expr2))
        else:
            tree =  union(parse(expr1), parse(expr2))
    
        print(encode(tree))

    except EOFError:
        break
