import sys

class Queue:
    def __init__(self, size):
        self.array = [0] * size
        self.fullness = 0
        self.first = 0
        self.last = 0

    def push(self, it, file):
        if self.fullness == len(self.array):
            file.write("overflow\n")
            return
        self.array[self.last] = it
        self.last = (self.last + 1) % len(self.array)
        self.fullness += 1
        return

    def pop(self, file):
        if self.fullness == 0:
            file.write("underflow\n")
            return
        file.write(str(self.array[self.first]) + '\n')
        self.array[self.first] = 0
        self.first = (self.first + 1) % len(self.array)
        self.fullness -= 1
        return

    def Print_Queue(self, file):
        if self.fullness == 0:
            file.write("empty\n")
        else:
            if self.first < self.last:
                    for i in range(self.first, self.last - 1):
                        file.write(str(self.array[i]) + ' ')
                    file.write(str(self.array[self.last - 1]) + '\n')
            elif self.first >= self.last:
                if self.last == 0:
                    for i in range(self.first, len(self.array) - 1):
                        file.write(str(self.array[i]) + ' ')
                    file.write(str(self.array[len(self.array) - 1]) + '\n')
                else:
                    for i in range(self.first, len(self.array)):
                        file.write(str(self.array[i]) + ' ')
                    for i in range(0, self.last - 1):
                        file.write(str(self.array[i]) + ' ')
                    file.write(str(self.array[self.last - 1]) + '\n')

readf = open(sys.argv[1], 'r')
writef = open(sys.argv[2], 'w')

while True:
    try:
        st = readf.readline()
        if st =='':
            readf.close()
            writef.close()
            sys.exit()
        if st[:9] == 'set_size ' and st[9:-1].isdigit():
            Queue = Queue(int(st[9:]))
            break
        elif st == '\n':
            continue
        else:
            writef.write("error\n")
    except EOFError:
        readf.close()
        writef.close()
        sys.exit()

while True:
    try:
        st = readf.readline()
        if st =='':
            readf.close()
            writef.close()
            sys.exit()
        if st[:5] == "push " and ' ' not in st[5:]:
            Queue.push(st[5:-1], writef)
        elif st == "pop\n" or st == "pop":
            Queue.pop(writef)
        elif st == "print\n" or st == "print":
            Queue.Print_Queue(writef)
        elif st == '\n':
            continue
        else:
            writef.write("error\n")
    except EOFError:
        writef.close()
        readf.close()
        sys.exit()


