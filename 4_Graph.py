import sys
from collections import deque

class Graph:
    def __init__(self, graph_type__, start_verdex__, search_type__):
        self.graph_table = dict()
        self.graph_type =  graph_type__
        self.start_verdex = start_verdex__
        self.search_type = search_type__

    def add (self, from_, to_):
        if from_ not in self.graph_table:
            self.graph_table.update({from_: [to_]})
        else:
            self.graph_table[from_].append(to_)
        if self.graph_type == 'u':
            if to_ not in self.graph_table:
                self.graph_table.update({to_: [from_]})
            else:
                 self.graph_table[to_].append(from_)
        else:
            if to_ not in self.graph_table:
                self.graph_table.update({to_: []})

    def with_search(self):
        unvisited = deque()
        visited = set()
        now = self.start_verdex
        unvisited.append(self.start_verdex)
        while len(unvisited) != 0:
            now = unvisited.popleft()
            if now in visited:
                continue
            else:
                visited.add(now)
            print(now)
            for i in sorted(self.graph_table[now]):
                if i not in visited:
                    unvisited.append(i)

    def depth_search(self):
        unvisited = deque()
        visited = set()
        now = self.start_verdex
        unvisited.append(self.start_verdex)
        while len(unvisited) != 0:
            now = unvisited.pop()
            if now in visited:
                continue
            else:
                visited.add(now)
            print(now)
            for i in reversed(sorted(self.graph_table[now])):
                unvisited.append(i)

type_g, start_v, search_t = input().split()
graph = Graph(type_g, start_v, search_t)

while True:
    try:
        st = input()
        if st == '':
            continue
        elif st == '\n':
            continue
        else:
            _from_, _to_ = st.split()
            graph.add(_from_, _to_)
    except EOFError:
        if search_t == 'd':
            graph.depth_search()
        else:
            graph.with_search()
        sys.exit()
