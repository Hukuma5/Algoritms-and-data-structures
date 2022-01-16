import sys
import math
from math import log2, log

class BitArray:
    def __init__(self, size):
        self.__size = size
        self.__num_of_blocks = (self.__size + 8 - 1) // 8
        self.__buf = [0] * self.__num_of_blocks

    def set_bit(self, i):
        block_ind = (i // 8)
        bit_ind = (i % 8)
        self.__buf[block_ind] |= (1 << (8 - 1 - bit_ind))

    def get_bit(self, i):
        block_ind = (i // 8)
        bit_ind = (i % 8)
        return self.__buf[block_ind] & (1 << (8 - 1 - bit_ind)) != 0

    def __str__(self):
        res = []
        for i in self.__buf:
            s = str(bin(i))[2:]
            if len(s) % 8 != 0:
                res.append('0' * (8 - len(s)))
            res.append(s)
        s = ''.join(str(x) for x in res)
        return s[:self.__size]

class Bloom_filter:

    def __primes_count(self, p, pr):
        k = round(-log2(p))
        pr.append(2)
        if k == 1:
            return pr
        num = 3
        while len(self.__primes) < k:
            if all(num % i != 0 for i in pr):
                pr.append(num)
            num += 2

    def __init__(self, size, p):
        self.__size = round(-size * log2(p)/log(2))
        self.__primes = []
        self.__primes_count(p, self.__primes)
        self.__bit_array = BitArray(self.__size)

    def add(self, key):
        for i in range(len(self.__primes)):
            h = (((i + 1) * key + self.__primes[i]) % (2 ** 31 - 1)) % self.__size
            self.__bit_array.set_bit(h)

    def search(self, key):
        for i in range(len(self.__primes)):
            h = (((i + 1) * key + self.__primes[i]) % (2 ** 31 - 1)) % self.__size
            if not self.__bit_array.get_bit(h):
                return False
        return True

    def get_m_and_k(self):
        return self.__size, len(self.__primes)

    def print(self, out):
        print(str(self.__bit_array), file=out)

out = sys.stdout
while True:
    try:
        line = input()
        if line == '':
            continue
        line = line.split()
        if len(line) == 3 and line[0] == 'set' \
                and line[1].isdigit() and int(line[1]) >= 1 \
                and float(line[2]) < 1 and float(line[2]) > 0 \
                and round(-int(line[1]) * log2(float(line[2])) / log(2)) >= 1 \
                and round(-log2(float(line[2]))) >= 1:
            break
        else:
            print('error', file=out)
            continue
    except EOFError:
        sys.exit()

size = int(line[1])
p = float(line[2])
bloom_filter = Bloom_filter(size, p)
m, k = bloom_filter.get_m_and_k()
print(m, k, file=out)
while True:
    try:
        line = input().split()
        if not line:
            continue
        elif line[0] == 'print':
            bloom_filter.print(out)
        elif len(line) == 2:
            if line[0] == 'add' and line[1].isdigit():
                bloom_filter.add(int(line[1]))
            elif line[0] == 'search' and line[1].isdigit():
                s = bloom_filter.search(int(line[1]))
                if s:
                    print('1', file=out)
                else:
                    print('0', file=out)
            else:
                print('error', file=out)
        else:
            print('error', file=out)
    except EOFError:
        sys.exit()
