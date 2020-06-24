while True:
    n_parts = [int(_) for _ in input().split() ]
    if n_parts[0]==0: break

    n_parts_all = n_parts[0]+n_parts[1]+n_parts[2]
    flag = [2]*n_parts_all

    n_results = int(input())
    results_trouble=[]
    for i in range(n_results):
        res=[int(_)-1 for _ in input().split()]
        has_trouble = res[3]==-1
        if has_trouble:
            results_trouble.append(res)
        else:
            flag[res[0]]=flag[res[1]]=flag[res[2]]=1
    
    while True:
        is_updated=False
        for r in results_trouble:
            for (i,j,k) in ((0,1,2),(1,2,0),(2,0,1)):
                if flag[r[i]]==1 and flag[r[j]]==1:
                    flag[r[k]]=0
                    is_update=True
        
        if not is_updated:
            break
    
    for f in flag:
        print(f)
