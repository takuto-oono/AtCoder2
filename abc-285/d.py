from typing import Dict


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


def main():
    n = int(input())
    name_dic: Dict[str, int] = {}
    num = 0
    union = UnionFind(2 * n)
    ans = 'Yes'
    for _ in range(n):
        s, t = input().split()
        if s not in name_dic.keys():
            name_dic[s] = num
            num += 1
        if t not in name_dic.keys():
            name_dic[t] = num
            num += 1
        if union.is_same(name_dic[s], name_dic[t]):
            ans = 'No'
        union.unite(name_dic[s], name_dic[t])

    print(ans)


if __name__ == '__main__':
    main()
