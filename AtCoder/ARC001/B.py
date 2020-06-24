A, B = list(map(int, input().split()))

queue = {0}
ans = 0
while B-A not in queue:
    ans += 1
    queue_new = set()
    for x in queue:
        queue_new |= {x+1, x-1, x+5, x-5, x+10, x-10}
    queue = queue_new
        
print(ans)
