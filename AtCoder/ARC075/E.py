class BTree:
  def __init__(self):
    self.root = 0
    self.keys = [[]]
    self.childs = [[None]]
    self.sizes = [0]
  
  def size(self, node):
    return 0 if node is None else self.sizes[node]

  # item <= keys[node][i] を満たす最小の(node, i, index)を返す
  # そのような(node, i)が存在しない場合は(None, None, None)を返す
  def bisect_left(self, item):
    retval = (None, None, None)
    index = 0
    node = self.root
    while node is not None:
      node_next = self.childs[node][-1]
      for i, (key, child) in enumerate(zip(self.keys[node], self.childs[node])):
        if item <= key:
          retval = (node, i, index + self.size(child))
          node_next = child
          break
        index += self.size(child) + 1
      node = node_next
    return retval
  
  # item < keys[node][i] を満たす最小の(node, i)を返す
  # そのような(node, i)が存在しない場合は(Nonde, None)を返す
  def bisect(self, item):
    retval = (None, None)
    node = self.root
    while node is not None:
      node_next = self.childs[node][-1]
      for i, (key, child) in enumerate(zip(self.keys[node], self.childs[node])):
        if item < key:
          retval = (node, i)
          node_next = child
          break
      node = node_next
    return retval

  # itemが挿入されるべき(node, i)のペアを返す
  def insert_path(self, item):
    path = []
    node = self.root
    while node is not None:
      p = (node, len(self.keys[node]))
      node_next = self.childs[node][-1]
      for i, (key, child) in enumerate(zip(self.keys[node], self.childs[node])):
        if item <= key:
          p = (node, i)
          node_next = child
          break
      path.append(p)
      node = node_next
    return path[::-1]
  
  def add(self, item):
    path = self.insert_path(item)
    lnode = rnode = None
    for layer, (node, i) in enumerate(path):
      keys = self.keys[node]
      childs = self.childs[node]
      keys.insert(i, item)
      childs.insert(i+1, rnode)
      self.sizes[node] = len(keys) + sum([self.size(child) for child in childs])

      if len(keys) < 4:
        for node, i in path[layer+1:]:
          self.sizes[node] += 1
        break

      item = keys[1]
      lkeys = keys[:1]
      lchilds = childs[:2]
      rkeys = keys[2:]
      rchilds = childs[2:]

      lnode = node
      self.keys[lnode] = lkeys
      self.childs[lnode] = lchilds
      self.sizes[lnode] = len(lkeys) + sum([self.size(child) for child in lchilds])

      rnode = len(self.keys)
      self.keys.append(rkeys)
      self.childs.append(rchilds)
      self.sizes.append(len(rkeys) + sum([self.size(child) for child in rchilds]))
    
    if lnode == self.root:
      self.root = len(self.keys)
      self.keys.append([item])
      self.childs.append([lnode, rnode])
      self.sizes.append(1 + self.size(lnode) + self.size(rnode))

  def __len__(self):
    return self.sizes[self.root]

  def __contains__(self, item):
    node, i, _ = self.bisect_left(item)
    return (node is not None) and (self.keys[node][i] == item)
  
  def __getitem__(self, index):
    if index < 0: return None

    node = self.root
    while node is not None:
      node_next = self.childs[node][-1]
      for key, child in zip(self.keys[node], self.childs[node]):
        if index < self.size(child):
          node_next = child
          break
        
        index -= self.size(child)
        if index==0: return key
        index -= 1

      node = node_next
    
    return None

N, K = map(int, input().split())
A = [int(input())-K for _ in range(N)]
s = 0
bt = BTree()
bt.add(0)
ans = N*(N+1)//2
for n, a in enumerate(A):
  s += a

  _, _, index = bt.bisect_left(s+1)
  if index is not None: ans -= len(bt) - index

  bt.add(s)

print(ans)