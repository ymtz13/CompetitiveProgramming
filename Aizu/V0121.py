d = [5040, 720, 120, 24, 6, 2, 1, 0]

def get_index(s):
    index=0
    used=[0]*8
    for digit in range(8):
        index+=(s[digit]-sum(used[:s[digit]])) * d[digit]
        used[s[digit]]=1
    return index

def move(s, loc_0):
    s_new=[]
    
    # move 0 vertical
    loc_0_v = (loc_0 + 4) % 8
    s_v = s.copy()
    s_v[loc_0], s_v[loc_0_v] = s_v[loc_0_v], s_v[loc_0]
    s_new.append((s_v, loc_0_v))

    # move 0 left
    if loc_0%4>0:
        loc_0_l = loc_0 - 1
        s_l = s.copy()
        s_l[loc_0], s_l[loc_0_l] = s_l[loc_0_l], s_l[loc_0]
        s_new.append((s_l, loc_0_l))

    # move 0 left
    if loc_0%4<3:
        loc_0_r = loc_0 + 1
        s_r = s.copy()
        s_r[loc_0], s_r[loc_0_r] = s_r[loc_0_r], s_r[loc_0]
        s_new.append((s_r, loc_0_r))

    return s_new

def search(s, loc_0, n):
    index_s = get_index(s)
    if memo[index_s] < n:
        return

    print(s, 'n({})'.format(n))
    memo[index_s] = n

    s_new_list = move(s, loc_0)
    for s_new in s_new_list:
        search(*s_new, n+1)

memo = [-1]*40320
memo[get_index([0,1,2,3,4,5,6,7])] = 0
queue = [([0,1,2,3,4,5,6,7], 0)]
n = 1
x = 0
while len(queue)>0:
    queue_new = []
    for s, loc_0 in queue:
        for s_new, loc_0_new in move(s, loc_0):
            if memo[get_index(s_new)] == -1:
                memo[get_index(s_new)] = n
                #print(s_new, 'n({})'.format(n))
                x+=1
                queue_new.append((s_new, loc_0_new))
                
    queue = queue_new
    n+=1

while True:
    try:
        s_input = [int(c) for c in input().split()]
        print(memo[get_index(s_input)])
                

    except EOFError:
        break
