class BTree:
  def __init__(self):
    self.root = 0
    self.keys = [[]]
    self.childs = [[None]]
    self.sizes = [0]
  
  # item <= keys[node][i] を満たす最小の(node, i)を返す
  # そのような(node, i)が存在しない場合は(Nonde, None)を返す
  def bisect_left(self, item):
    retval = (None, None)
    node = self.root
    while node is not None:
      node_next = self.childs[node][-1]
      for i, (key, child) in enumerate(zip(self.keys[node], self.childs[node])):
        if item <= key:
          retval = (node, i)
          node_next = child
          break
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

    def size(node):
      return 0 if node is None else self.sizes[node]

    rnode = None
    for layer, (node, i) in enumerate(path):
      keys = self.keys[node]
      childs = self.childs[node]
      keys.insert(i, item)
      childs.insert(i+1, rnode)
      self.sizes[node] = len(keys) + sum([size(node) for child in childs])

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
      self.sizes[lnode] = len(lkeys) + sum([size(child) for child in lchilds])

      rnode = len(self.keys)
      self.keys.append(rkeys)
      self.childs.append(rchilds)
      self.sizes.append(len(rkeys) + sum([size(child) for child in rchilds]))
    
    if lnode == self.root:
      print('add new root')
      self.root = len(self.keys)
      self.keys.append([item])
      self.childs.append([lnode, rnode])
      self.sizes.append(1 + size(lnode) + size(rnode))

  def __contains__(self, item):
    node, i = self.bisect_left(item)
    return (node is not None) and (self.keys[node][i] == item)
  
  def __getitem__(self, index):
    if index < 0: return None

    def size(node):
      return 0 if node is None else self.sizes[node]

    node = self.root
    while node is not None:
      node_next = self.childs[node][-1]
      for key, child in zip(self.keys[node], self.childs[node]):
        if index < size(child):
          node_next = child
          break
        
        index -= size(child)
        if index==0: return key
        index -= 1

      node = node_next
    
    return None


Q = int(input())
bt = Btree()
for _ in range(Q):
  T, X = map(int, input().split())
  if T==1: bt.add(X)
      