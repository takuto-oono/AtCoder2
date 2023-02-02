from typing import List


class UnionFind:
    def __init__(self, n: int) -> None:
        self.parents = [-1 for _ in range(n)]
        self.sizes = [1 for _ in range(n)]

    def get_parent(self, x: int) -> int:
        if self.parents[x] == -1:
            return x
        self.parents[x] = self.get_parent(self.parents[x])
        return self.parents[x]

    def is_same(self, x: int, y: int) -> bool:
        return self.get_parent(x) == self.get_parent(y)

    def unite(self, x: int, y: int) -> bool:
        x, y = self.get_parent(x), self.get_parent(y)
        if x == y:
            return False
        if self.sizes[x] < self.sizes[y]:
            x, y = y, x
        self.parents[y] = x
        self.sizes[x] += self.sizes[y]
        return True

    def get_size(self, x: int) -> int:
        return self.sizes[self.get_parent(x)]

    def get_parents_count(self) -> int:
        cnt = 0
        for parent in self.parents:
            if parent == -1:
                cnt += 1
        return cnt

    def get_parents_list(self) -> List[int]:
        parents_list = []
        for i, p in enumerate(self.parents):
            if p == -1:
                parents_list.append(i)
        return parents_list
