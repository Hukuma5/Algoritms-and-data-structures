import sys

class Trie:
    def __init__(self):
        self.__head = {}
        self.__end = False
    '''
    Добавление слова в дерево
    Сложность этого алгоритма по времени O(n), где n - длина слова, т.к. каждую букву введенного слова нужно проверить на наличие в дереве,
    а если такой буквы нет, то начиная с этой буквы добавляем все следующие
    Сложность алгоритма по памяти O(n), т.к. если введенной буквы нет в дереве, её нужно туда добавить
    '''
    def add(self, word):
        current = self
        for i, ch in enumerate(word):
            if ch not in current.__head:
                current.__head[ch] = Trie()
            current = current.__head[ch]
            if i == len(word) - 1:
                current.__end = True

    '''
    Сложность алгоритма коррекции по времени O(n*m), где n - длина входного слова, а m - колличество узлов в дереве.
    Сложность алгоритма коррекции по памяти O(n*m), где n - длина слова,
    а m - колличество узлов в словаре, т.к. для обхода каждого узла требуется рекурсивный вызов, следовательно заполняется стек вызовов а для проверки каждого узла требуется
    3 строки матрицы
    '''
    @staticmethod
    def correction(cur, buf, symb, prev_symb, word, pre_row, pre_pre_row, result):
        if cur is None:
            return
        columns = len(word) + 1
        current_row = [pre_row[0] + 1]

        for column in range(1, columns):
            if word[column - 1] == symb:
                min_cost = min(pre_row[column] + 1, current_row[column - 1] + 1, pre_row[column - 1])
            else:
                min_cost = min(pre_row[column] + 1, current_row[column - 1] + 1, pre_row[column - 1] + 1)

            current_row.append(min_cost)

            if prev_symb is not None and \
                    column > 1 and \
                    symb == word[column - 2] and \
                    prev_symb == word[column - 1] and \
                    word[column - 1] != symb:
                current_row[column] = min(current_row[column], pre_pre_row[column - 2] + 1)

        if current_row[-1] == 1 and cur.__end:
            result.append(buf)

        if min(current_row) <= 1:
            prev_symbol_ = symb

            for symb, child_ in cur.__head.items():
                Trie.correction(child_, buf + symb, symb, prev_symbol_, word, current_row, pre_row, result)

    '''
    Сложность по времени алгоритма поиска (без автокоррекции) - O(n),
    где n - длина искомого слова, т.к. нужно проверить, что каждый 
    символ искомого слова есть в дереве
    Сложность по памяти - O(1), т.к. при обходе ветви дополнителььная 
    память не выделяется
    '''
    def search(self, word):
        res = []
        current = self
        same = True
        current_row = range(len(word) + 1)
        for ch in word:
            if ch in current.__head:
                current = current.__head[ch]
            else:
                same = False
                break
        if current.__end == False:
            same = False
        if not same:
            for letter, ch in self.__head.items():
                self.correction(ch, letter, letter, None, word, current_row, None, res)
        if res:
            return sorted(res)
        elif same:
            m = []
            m.append(True)
            return m
        else:
            return None

out = sys.stdout
my_trie = Trie()
size_of_dictionary = int(input())
Enter = False

for _ in range(size_of_dictionary):
    word = input().lower()
    my_trie.add(word)

for line in sys.stdin:
    if line == '\n':
        continue
    line = line[:-1]
    if Enter:
        print(file=out)
    else:
        Enter = True
    x = my_trie.search(line.lower())
    if x is None:
        print(line + ' -?', end='', file=out)
    elif x[0] == True:
        print(line + ' - ok', end='', file=out)
    else:
        print(line + ' -> ', end='', file=out)
        for i in range(len(x) - 1):
            print(x[i], end=', ', file=out)
        print(x[-1], end='', file=out)
