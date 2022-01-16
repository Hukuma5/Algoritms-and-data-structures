import sys
import math

class Backpack:
    def __init__(self):
        self.__things = {}
        self.__weight_of_things = 0
        self.__cost_of_things = 0
        self.__res = []

    class thing:
        def __init__(self, w, c):
            self.weight = w
            self.cost = c

    def add(self, weight, cost):
        self.__things[len(self.__things)] = self.thing(weight, cost)

    def __copy_nod(self, max_weight):
        nod = math.gcd(self.__things[0].weight, max_weight)
        if len(self.__things) != 1:
            for i in range(1, len(self.__things)):
                nod = math.gcd(nod, self.__things[i].weight)
        weight = []
        cost = []
        for i in self.__things:
            weight.append(int(self.__things[i].weight / nod))
            cost.append(self.__things[i].cost)
        return weight, cost, nod

    def __create_matrix(self, matrix, max_weight, weight, cost):
        for i in range(len(self.__things) + 1):
            for j in range(max_weight + 1):
                if i == 0:
                    continue
                elif weight[i - 1] <= j:
                    matrix[i][j] = max(cost[i - 1] + matrix[i - 1][j - weight[i - 1]], matrix[i - 1][j])
                else:
                    matrix[i][j] = matrix[i - 1][j]
        return

    def get_result(self, max_weight):
        weight, cost, nod = self.__copy_nod(max_weight)
        max_weight = int(max_weight / nod)
        matrix = [[0 for w in range(max_weight + 1)] for i in range(len(self.__things) + 1)]

        self.__create_matrix(matrix, max_weight, weight, cost)
        res = []
        weight_of_things = 0
        cost_of_things = matrix[len(self.__things)][max_weight]
        for i in range(len(self.__things), 0, -1):
            if cost_of_things == 0:
                break
            elif cost_of_things == matrix[i - 1][max_weight]:
                continue
            else:
                res.append(i)
                max_weight -= weight[i - 1]
                cost_of_things -= cost[i - 1]
                weight_of_things += weight[i - 1]
        self.__weight_of_things = weight_of_things * nod
        self.__cost_of_things = matrix[-1][-1]
        self.__res = sorted(res)
        return weight_of_things * nod, matrix[-1][-1], self.__res

    def print(self, out):
        if len(self.__things) == 0:
            return
        print(self.__weight_of_things, self.__cost_of_things, file=out)
        for i in range(len(self.__res)):
            print(self.__res[i], file=out)

backpack = Backpack()
out = sys.stdout
while True:
    line = input()
    if not line:
        continue
    elif len(line.split()) != 1:
        print('error', file=out)
        continue
    else:
        break
max_weight = int(line)
while True:
    try:
        line = input().split()
        if not line:
            continue
        elif len(line) == 1:
            print('error', file=out)
            continue
        if line[0].isdigit() and line[1].isdigit() and int(line[0]) >= 0 and int(line[1]) >= 0:
            backpack.add(int(line[0]), int(line[1]))
        else:
            print('error', file=out)
    except EOFError:
        break

backpack.get_result(max_weight)
backpack.print(out)
