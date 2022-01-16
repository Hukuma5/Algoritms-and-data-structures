from collections import deque
import sys

class SplayTree:
  class __Node:
    def __init__(self, key, value, parent):
      self._left   = None
      self._right  = None
      self._parent = parent
      self._key    = key
      self._value = value

  def __init__(self):
    self.__root = None

  def __rotate(self, x):
    if x._parent._right == x:
      x._parent._right = x._left
      if x._left is not None:
        x._left._parent = x._parent
      x._left = x._parent

    if x._parent._left == x:
      x._parent._left = x._right
      if x._right is not None:
        x._right._parent = x._parent
      x._right = x._parent

    grandpa = x._parent._parent
    if grandpa is not None and grandpa._right == x._parent:
      grandpa._right = x
    elif grandpa is not None and grandpa._left == x._parent:
      grandpa._left = x
    else:
      self.__root = x
    x._parent._parent = x
    x._parent = grandpa

  def __splay(self, node):
    while node._parent is not None:
      if node._parent._parent is None:
        self.__rotate(node)
      elif (node == node._parent._left and node._parent ==
             node._parent._parent._left) or (node == node._parent._right and node._parent ==
                                   node._parent._parent._right):
        self.__rotate(node._parent)
        self.__rotate(node)
      else:
        self.__rotate(node)
        self.__rotate(node)

  def __find(self, v, key):
    if self.__root == None:
      return None
    if key == v._key:
      self.__splay(v)
      return v._value
    if key < v._key and v._left != None:
      return self.__find(v._left, key)
    if key > v._key and v._right != None:
      return self.__find(v._right, key)
    self.__splay(v)
    return None

  def found(self, key):
    return self.__find(self.__root, key)

  def insert(self, key, value):
    if self.__root is None:
      self.__root = self.__Node(key, value, None)
      return True
    current = self.__root
    while current is not None:
      if current._key == key:
        self.__splay(current)
        return False
      if current._key > key:
        if current._left is None:
          current._left = self.__Node(key, value, current)
          current._left._parent = current
          self.__splay(current._left)
          break
        else:
          current = current._left
      elif current._key < key:
        if current._right is None:
          current._right = self.__Node(key, value, current)
          current._right._parent = current
          self.__splay(current._right)
          break
        else:
          current = current._right
      else:
          return False
    return True

  def remove(self, key):
    if self.__root is None:
      return False
    current = self.__root
    while current is not None:
      if current._key > key:
        if current._left is None:
          self.__splay(current)
          return False
        current = current._left
      elif current._key < key:
        if current._right is None:
          self.__splay(current)
          return False
        current = current._right
      elif current._key == key:
        self.__splay(current)
        break
      else:
        return False
    if current is None:
      return False

    left_tree = current._left
    right_tree = current._right
    if left_tree is not None:
      left_tree._parent = None
    if right_tree is not None:
      right_tree._parent = None
    if left_tree is None:
      self.__root = right_tree
    elif right_tree is None:
      self.__root = left_tree
    else:
      self.__root = left_tree
      current = left_tree
      while current._right is not None:
        current = current._right
      self.__splay(current)
      current._right = right_tree
      right_tree._parent = current
    return True

  def set(self, key, value):
    if self.__root == None:
      return False
    else:
      self.__find(self.__root, key)
      if self.__root._key == key:
        self.__root._value = value
        self.__root._value = value
      else:
        return False

  def __Depth_(self, node):
    if node:
      return 1 + max(self.__Depth_(node._left), self.__Depth_(node._right))
    return 0

  def __Depth(self):
    return self.__Depth_(self.__root)

  def print_tree(self, out):
    if self.__root == None:
      print('_', file=out)
      return
    print('[', end='', file=out)
    print(self.__root._key, self.__root._value, end=']\n', file=out)
    if self.__root._left is None and self.__root._right is None:
      return

    unvisited = deque()
    if self.__root._left is not None:
      unvisited.append(self.__root._left)
    else:
      unvisited.append(1)
    if self.__root._right is not None:
      unvisited.append(self.__root._right)
    else:
      unvisited.append(1)

    number = 0
    i_node = 0
    number_of_nodes = 2
    level_counter = 2
    line = ''
    while len(unvisited) != 0:
      number += 1
      node = unvisited.popleft()
      if type(node) != int:
        line += '['
        line += '{}'.format(node._key)
        line += ' ' + node._value + ' '
        line += '{}'.format(node._parent._key)
        line += '] '
        i_node += 1
        if node._left is not None:
          unvisited.append(node._left)
        else:
          unvisited.append(1)
        if node._right is not None:
          unvisited.append(node._right)
        else:
          unvisited.append(1)
      else:
        for i in range(node):
          line += '_ '
        i_node += node
        unvisited.append(node * 2)

      if i_node == number_of_nodes:
        i_node = 0
        if line[-1] == ' ':
          line = line[:-1]
        print(line, file=out)
        line = ''
        number_of_nodes *= 2
        level_counter += 1

      if level_counter - 1 == self.__Depth() and i_node == 0:
        break

  def min(self):
    if self.__root is None:
      return None, None
    node = self.__root
    while node._left is not None:
      node = node._left
    self.__splay(node)
    return node._key, node._value

  def max(self):
    if self.__root is None:
      return None, None
    node = self.__root
    while node._right is not None:
      node = node._right
    self.__splay(node)
    return node._key, node._value

tree = SplayTree()
out = sys.stdout
sys.setrecursionlimit(10000)
while True:
    try:
        str = input().split()
        if not str:
          continue
        if str[0] == 'add':
          s = tree.insert(int(str[1]), str[2])
          if s == False:
            print('error', file=out)
        elif str[0] == 'set':
          s = tree.set(int(str[1]), str[2])
          if s == False:
            print('error', file=out)
        elif str[0] == 'search':
          s = tree.found(int(str[1]))
          if s is None:
            print('0', file=out)
          else:
            print('1', s, file=out)
        elif str[0] == 'delete':
          s = tree.remove(int(str[1]))
          if s == False:
            print('error', file=out)
        elif str[0] == 'print':
          tree.print_tree(out)
        elif str[0] == 'min':
          a, b = tree.min()
          if a is None:
            print('error', file=out)
          else:
            print(a, b, file=out)
        elif str[0] == 'max':
          a, b = tree.max()
          if a is None:
            print('error', file=out)
          else:
            print(a, b, file=out)
        else:
          print('error', file=out)

    except EOFError:
        sys.exit()
