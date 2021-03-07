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

def test1():
  bt = BTree()
  bt.keys = [
    [5, 9],
    [1, 3],
    [5],
    [9, 11],
    [1],
    [1],
    [3, 4],
    [5],
    [9],
    [9],
    [9],
    [12],
  ]
  bt.childs = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8],
    [9, 10, 11],
    [None, None],
    [None, None],
    [None, None, None],
    [None, None],
    [None, None],
    [None, None],
    [None, None],
    [None, None],
  ]
  bt.parents = [
    (None, None),
    (0, 0),
    (0, 1),
    (0, 2),
    (1, 0),
    (1, 1),
    (1, 2),
    (2, 0),
    (2, 1),
    (3, 0),
    (3, 1),
    (3, 2),
  ]

  for i in range(0, 14):
    print(
      '{:2d}'.format(i), 
      bt.bisect_left(i),
      bt.bisect(i),
      bt.insert_path(i),
      i in bt
    )

def test2():
  bt = BTree()
  bt.keys = [
    [1, 6, 7],
    [1], 
    [2, 3, 5],
    [6],
    [7],
  ]
  bt.childs = [
    [1, 2, 3, 4],
    [None, None],
    [None, None, None, None],
    [None, None],
    [None, None],    
  ]
  bt.sizes = [
    9,
    1,
    3,
    1,
    1,
  ]

  for i in range(0, 8):
    print(
      '{:2d}'.format(i), 
      bt.bisect_left(i),
      bt.bisect(i),
      bt.insert_path(i),
      i in bt
    )
  print(bt.keys)

  bt.add(4)
  print(bt.keys)
  print(bt.childs)
  print(bt.root)
  print(bt.sizes)
  for i in range(-1, 12):
    print(i, bt[i])

test2()