N, K = [int(c) for c in input().split()]
V = [int(c) for c in input().split()]

max_value = 0
r_nega, r_posi = [],0
for n_take_r in range(min(K+1, N+1)):    
    if n_take_r >= 1:
        v_take = V[N-n_take_r]
        if v_take < 0: r_nega.append(v_take)
        else: r_posi += v_take
        
    l_nega, l_posi = [],0
    for n_take_l in range(min(K+1, N+1)-n_take_r):
        if n_take_l >= 1:
            v_take = V[n_take_l-1]
            if v_take < 0: l_nega.append(v_take)
            else: l_posi += v_take

        n_remove = K - n_take_r - n_take_l
        value = r_posi + l_posi + sum(sorted(r_nega+l_nega)[n_remove:])
        max_value = max(max_value, value)

print(max_value)
        

        
