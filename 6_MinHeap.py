import sys
import math

class MinHeap:
    def __init__(self):
        self.__array = []
        self.__ind = {}

    class __Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value

    def __up(self, i):
        i_parent = (i - 1) // 2
        if i != 0 and self.__array[i].key < self.__array[i_parent].key:
            self.__ind[self.__array[i].key] = i_parent
            self.__ind[self.__array[i_parent].key] = i
            self.__array[i], self.__array[i_parent] = self.__array[i_parent], self.__array[i]
            self.__up(i_parent)

    def add(self, i, v):
        if i in self.__ind:
            return False
        if not self.__array:
            self.__array.append(self.__Node(i, v))
            self.__ind[i] = 0
        else:
            self.__array.append(self.__Node(i, v))
            self.__ind[i] = len(self.__array) - 1
            self.__up(self.__ind[i])

    def set(self, key, value):
        if key not in self.__ind:
            return False
        i = self.__ind[key]
        self.__array[i].value = value

    def __down(self, i):
        min_i = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(self.__array) and self.__array[min_i].key > self.__array[left].key:
            min_i = left
        if right < len(self.__array) and self.__array[min_i].key > self.__array[right].key:
            min_i = right
        if min_i != i:
            self.__ind[self.__array[i].key] = min_i
            self.__ind[self.__array[min_i].key] = i
            self.__array[i], self.__array[min_i] = self.__array[min_i], self.__array[i]
            self.__down(min_i)

    def delete(self, key):
        if key not in self.__ind:
            return False
        i = self.__ind[key]

        if len(self.__array) > 1 and i < len(self.__array) - 1:
            del self.__ind[key]
            self.__ind[self.__array[len(self.__array) - 1].key] = i
            self.__array[i] = self.__array[len(self.__array) - 1]
            self.__array.pop()
            parent = (i - 1) // 2
            if self.__array[i].key > self.__array[parent].key:
                self.__down(i)
            else:
                self.__up(i)
            self.__down(0)
        else:
            del self.__ind[key]
            self.__array.pop()

    def search(self, key):
        if key not in self.__ind or not self.__array:
            return None, None
        return self.__ind[key], self.__array[self.__ind[key]].value

    def min_(self):
        if not self.__array:
            return None, None, None
        return self.__array[0].key, 0, self.__array[0].value

    def max_(self):
        if not self.__array:
            return None, None, None
        max = self.__array[0]
        max_i = 0
        for i in range(len(self.__array) // 2, len(self.__array)):
            if self.__array[i].key > max.key:
                max = self.__array[i]
                max_i = i
        return max.key, max_i, max.value

    def extract(self):
        if not self.__ind:
            return None, None
        key = self.__array[0].key
        value = self.__array[0].value
        self.delete(self.__array[0].key)
        return key, value

    def print_heap(self, out):
        if not self.__array:
            print('_', file=out)
            return
        print('[', end='', file=out)
        print(self.__array[0].key, self.__array[0].value, end=']\n', file=out)
        for i in range(1, math.floor(math.log2(len(self.__array))) + 1):
            start_i = 2 ** i - 1
            len_ = 2 ** (i + 1) - 1
            end_of_print = ' '
            for j in range(start_i, len_):
                if j > len(self.__array) - 1:
                    if j == len_ - 1:
                        end_of_print = ''
                    print('_', end=end_of_print, file=out)
                else:
                    if j == len_ - 1:
                        end_of_print = ''
                    parent_ind = (j - 1) // 2
                    print('[', end='', file=out)
                    print(self.__array[j].key, self.__array[j].value, self.__array[parent_ind].key, end=']' + end_of_print, file=out)
            print(file=out)

heap = MinHeap()
out = sys.stdout

while True:
    try:
        str = input().split()
        if not str:
            continue
        if str[0] == 'add':
            s = heap.add(int(str[1]), str[2])
            if s == False:
                print('error', file=out)
        elif str[0] == 'set':
            s = heap.set(int(str[1]), str[2])
            if s == False:
                print('error', file=out)
        elif str[0] == 'search':
            if len(str) < 2:
                print('error', file=out)
            a, b = heap.search(int(str[1]))
            if a is None:
                print('0', file=out)
            else:
                print('1', a, b, file=out)
        elif str[0] == 'delete':
            s = heap.delete(int(str[1]))
            if s == False:
                print('error', file=out)
        elif str[0] == 'print':
            heap.print_heap(out)
        elif str[0] == 'min':
            a, b, c = heap.min_()
            if a is None:
                print('error', file=out)
            else:
                print(a, b, c, file=out)
        elif str[0] == 'max':
            a, b, c = heap.max_()
            if a is None:
                print('error', file=out)
            else:
                print(a, b, c, file=out)
        elif str[0] == 'extract':
            a, b = heap.extract()
            if a is None:
                print('error', file=out)
            else:
                print(a, b, file=out)
        else:
            print('error', file=out)

    except EOFError:
        sys.exit()
