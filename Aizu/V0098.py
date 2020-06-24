n=int(input())
matrix=[[0]*(n+1)]
for i in range(1,n+1):
    row = [0]+[int(e) for e in input().split()]
    for j in range(1,n+1):
        row[j]+=row[j-1]        
    matrix.append(row)

    for j in range(n+1):
        matrix[i][j] += matrix[i-1][j]

#print(matrix)
m=matrix[1][1]
for row_end in range(n+1):
    for row_bgn in range(row_end):
        s =[matrix[row_end][col]-matrix[row_bgn][col] for col in range(n+1)]
        ma=[s[col] - min(s[:col])for col in range(1,n+1)]
        print(row_bgn, row_end, s, ma, max(ma))
        m=max(m,max(ma))

print(m)

# 0  0 0 0 
# 0  3 5 6
# 0  1 3 7
# 0 -2 1 1

# 0  0  0  0 
# 0  3  8 14
# 0  4 12 25
# 0  2 11 25
