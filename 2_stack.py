import sys


class Stack:
    def __init__(self, size):
        self.array = [0] * size
        self.iterator = 0

    def push(self, it):
        if self.iterator == len(self.array):
            print("overflow")
            return
        self.array[self.iterator] = it
        self.iterator += 1
        return

    def pop(self):
        if self.iterator == 0:
            print("underflow")
            return
        print(self.array[self.iterator - 1])
        self.array[self.iterator - 1] = 0
        self.iterator -= 1
        return

    def Print_Stack(self):
        if self.iterator == 0:
            print("empty")
        else:
            for i in range(self.iterator - 1):
                print(self.array[i], end=' ')
            print(self.array[self.iterator - 1])


while True:
    try:
        str = input()
        if str[:9] == 'set_size ' and str[9:].isdigit():
            Stac = Stack(int(str[9:]))
            break
        elif str == '':
            continue
        else: print("error")
    except EOFError:
        sys.exit()
while True:
    try:
        str = input()
        if str[:5] == "push " and ' ' not in str[5:]:
            Stac.push(str[5:])
        elif str == "pop":
            Stac.pop()
        elif str == "print":
            Stac.Print_Stack()
        elif str == '':
            continue
        else:
            print("error")
    except EOFError:
        sys.exit()

