from array import array

class HeapQueue:
  _array_extend_size = 100
  _padding = (0, )*_array_extend_size

  def __init__(self, typecode='q'):
    self.length = 0
    self.data = array(typecode, self._padding)

    self.next_key = 0
    self.keys = array('Q', self._padding) # index to key map
    self.poss = array('Q', self._padding) # key to index map
  
  def push(self, value):
    index = self.length + 1
    key = self.next_key

    if len(self.data) == index:
      self.data.extend(self._padding)
      self.keys.extend(self._padding)
    if len(self.poss) == key:
      self.poss.extend(self._padding)

    self.data[index] = value
    self.keys[index] = key
    self.poss[key] = index

    self._bubble_up(index)

    self.length += 1
    self.next_key += 1

    return key

  def pop(self, key=None):
    index = 1 if key is None else self.poss[key]

    retval = (self.keys[index], self.data[index])

    index_last = self.length
    if index < index_last:
      key_last = self.keys[index_last]
      self.keys[index] = key_last
      self.poss[key_last] = index
      self.update(key_last, self.data[index_last])
    
    self.length -= 1
    return retval

  def update(self, key, value):
    index = self.poss[key]
    value_old = self.data[index]
    self.data[index] = value

    if value < value_old:
      self._bubble_up(index)
    
    if value > value_old:
      self._bubble_down(index)

  def _bubble_up(self, index):
    value = self.data[index]
    key = self.keys[index]

    while True:
      index_parent = index >> 1
      value_parent = self.data[index_parent]

      if value < value_parent:
        key_parent = self.keys[index_parent]
        self.data[index] = value_parent
        self.keys[index] = key_parent
        self.poss[key_parent] = index

        index = index_parent

      else:
        break
    
    self.data[index] = value
    self.keys[index] = key
    self.poss[key] = index

  def _bubble_down(self, index):
    value = self.data[index]
    key = self.keys[index]

    while True:
      index_lchild = index << 1
      index_rchild = index_lchild + 1
      if index_lchild > self.length: break

      value_lchild = self.data[index_lchild]
      value_rchild = self.data[index_rchild] if index_rchild <= self.length else value_lchild + 1

      if   value_lchild <= value_rchild and value_lchild < value:
        key_lchild = self.keys[index_lchild]
        self.data[index] = value_lchild
        self.keys[index] = key_lchild
        self.poss[key_lchild] = index

        index = index_lchild

      elif value_rchild <= value_lchild and value_rchild < value:
        key_rchild = self.keys[index_rchild]
        self.data[index] = value_rchild
        self.keys[index] = key_rchild
        self.poss[key_rchild] = index

        index = index_rchild

      else:
        break
    
    self.data[index] = value
    self.keys[index] = key
    self.poss[key] = index

  def _swap(self, index1, index2):
    value1 = self.data[index1]
    value2 = self.data[index2]
    key1 = self.keys[index1]
    key2 = self.keys[index2]

    self.data[index1] = value2
    self.data[index2] = value1
    self.keys[index1] = key2
    self.keys[index2] = key1
    self.poss[key1] = index2
    self.poss[key2] = index1

  def peek(self):
    return self.data[1]
  
  def __len__(self):
    return self.length


hq = HeapQueue()

items = [4,5,8,2,6,0,1,9,3,7]*100000
for key, item in enumerate(items):
  hq.push(item)


print(hq.data[:64])
print(hq.pop())
print(hq.pop())
print(hq.pop(3))
print(hq.pop())
