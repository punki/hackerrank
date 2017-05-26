#!/bin/python3

import sys


class UFQuickFind:
    def __init__(self, n) -> None:
        self.count = n
        self.roads = 0
        self.id = [i for i in range(n)]

    def union(self, p, q):
        pId = self.find(p)
        qId = self.find(q)
        if pId == qId:
            return

        for i in range(n):
            if self.id[i] == pId:
                self.id[i] = qId
        self.roads += 1
        self.count -= 1

    def find(self, p):
        return self.id[p]

    def connected(self, p, q):
        return self.find(p) == self.find(q)


class UFQuickUnion:
    def __init__(self, n) -> None:
        self.count = n
        self.roads = 0
        self.id = [i for i in range(n)]

    def union(self, p, q):
        pId = self.find(p)
        qId = self.find(q)
        if pId == qId:
            return

        self.id[pId] = qId

        self.roads += 1
        self.count -= 1

    def find(self, p):
        while p != self.id[p]:
            p = self.id[p]
        return p

    def connected(self, p, q):
        return self.find(p) == self.find(q)


class UFWeightedQuickUnion:
    def __init__(self, n) -> None:
        self.count = n
        self.sz = [1 for i in range(n)]
        self.roads = 0
        self.id = [i for i in range(n)]

    def union(self, p, q):
        pId = self.find(p)
        qId = self.find(q)
        if pId == qId:
            return

        if self.sz[pId] < self.sz[qId]:
            self.id[pId] = qId
            self.sz[qId] += self.sz[pId]
        else:
            self.id[qId] = pId
            self.sz[pId] += self.sz[qId]

        self.roads += 1
        self.count -= 1

    def find(self, p):
        while p != self.id[p]:
            p = self.id[p]
        return p

    def connected(self, p, q):
        return self.find(p) == self.find(q)


q = int(input().strip())
for a0 in range(q):
    n, m, x, y = input().strip().split(' ')
    n, m, lib_cost, road_cost = [int(n), int(m), int(x), int(y)]
    cost = 0
    if lib_cost < road_cost:
        for a1 in range(m):
            city_1, city_2 = input().strip().split(' ')
            city_1, city_2 = [int(city_1) - 1, int(city_2) - 1]
        cost = n * lib_cost
    else:
        uf = UFWeightedQuickUnion(n)
        for a1 in range(m):
            city_1, city_2 = input().strip().split(' ')
            city_1, city_2 = [int(city_1) - 1, int(city_2) - 1]
            uf.union(city_1, city_2)

        # print("roads: {0}".format(uf.roads))
        # print("count: {0}".format(uf.count))
        cost = uf.count * lib_cost + uf.roads * road_cost
    print(cost)
