H, W = list(map(int, input().split()))
M = []
M.append('.'*(W+2))
M += ['.'+input()+'.' for _ in range(H)]
M.append('.'*(W+2))

for h in range(1, H+1):
    for w in range(1,W+1):
        if M[h][w]=='#' and ('....'==M[h][w+1]+M[h][w-1]+M[h+1][w]+M[h-1][w]):
            print('No')
            exit()

print('Yes')
                             
