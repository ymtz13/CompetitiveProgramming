class MultiSet:
  LEFT = 1
  RIGHT = 2

  def __init__(self):
    self.n = [0]  # 部分木のサイズ
    self.values = [None]
    self.lc = [None]  # 左子ノードのインデックス
    self.rc = [None]  # 右子ノードのインデックス
    self.root = 0  # 根ノードのインデックス

    self.parent = [None]  # 親ノードのインデックス
    self.lr = [None]  # 自身が左子ノードか右子ノードか

    self.deleted = [False]  # 削除されたノード

  def add(self, value):
    i = self.root
    while self.n[i] > 0:
      self.n[i] += 1
      i = self.lc[i] if value < self.values[i] else self.rc[i]

    self.n[i] = 1
    self.values[i] = value
    ilc = len(self.n)
    irc = ilc + 1
    self.lc[i] = ilc
    self.rc[i] = irc

    self.n.extend((0, 0))
    self.values.extend((None, None))
    self.lc.extend((None, None))
    self.rc.extend((None, None))
    self.parent.extend((i, i))
    self.parent.extend((MultiSet.LEFT, MultiSet.RIGHT))

  def remove(self, value):
    i = self.root
    target = None
    while self.n[i] > 0:
      if self.values[i] == value:
        target = i
        break
      i = self.lc[i] if value < self.values[i] else self.rc[i]

    if target is None: return False

    lchild = self.lc[target]
    rchild = self.rc[target]
    nchild = 2 - (lchild, rchild).count(None)

    if nchild == 0:
      self.n[target] = 0
      self.values[target] = None
      self.lc[target] = None
      self.rc[target] = None

    elif nchild == 1:
      child = lchild if lchild is not None else rchild
      par = self.parent[target]
      self.parent[child] = par

      if self.lr[target] == MultiSet.LEFT:
        self.lc[par] = child
        self.lr[child] = MultiSet.LEFT
      
      else:
        self.rc[par] = child
        self.lr[child] = MultiSet.RIGHT
    
    else:
      pass

    # modify ancestors

  def contain(self, value):
    i = self.root
    while self.n[i] > 0:
      if self.values[i] == value: return True
      i = self.lc[i] if value < self.values[i] else self.rc[i]

    return False

  def __str__(self):
    s = []

    stack = [(self.root, 0)]
    while stack:
      i, indent = stack.pop()
      s.append('{}[{:2d}] {}'.format('  ' * indent, i, self.values[i]))

      if self.n[i] > 0:
        stack.append((self.rc[i], indent + 1))
        stack.append((self.lc[i], indent + 1))

    return '\n'.join(s)


ms = MultiSet()

print(ms)
for x in (4, 8, 3, 9, 8, 2):
  print()
  print('ADD', x)
  ms.add(x)
  print(ms)

for x in range(10):
  print('CONTAIN', x, ms.contain(x))
