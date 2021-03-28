from priority_queue import HeapQueue
from time import time

hq = HeapQueue()

items = [4,5,8,2,6,0,1,9,3,7]*100000
bgn = time()
for key, item in enumerate(items):
  hq.push(item)
end = time()

bgn2 = time()
for key, item in enumerate(items):
  hq.push(item)
  hq.pop()
end2 = time()

print(end - bgn)
print(end2 - bgn2)
