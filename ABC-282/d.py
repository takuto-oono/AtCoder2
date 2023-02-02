from typing import List, Tuple, Dict
from collections import deque


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


def dfs(start: int, branch: List[List[int]]) -> Tuple[int, int]:
    todo_list: deque[Tuple[int, int]] = deque([(start, 1)])
    numbers_dic: Dict[int, int] = {}
    while len(todo_list) > 0:
        (now, num) = todo_list.popleft()
        if now in numbers_dic.keys():
            if numbers_dic[now] != num:
                return (0, 0)
            continue
        numbers_dic[now] = num
        for next in branch[now]:
            todo_list.append((next, num * -1))

    cnt_1, cnt_2 = 0, 0
    for _, v in numbers_dic.items():
        if v == 1:
            cnt_1 += 1
        if v == -1:
            cnt_2 += 1
    return (cnt_1, cnt_2)


def main():
    n, m = map(int, input().split())
    branch: List[List[int]] = [[] for _ in range(n)]
    unionFind = UnionFind(n)
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        branch[v].append(u)
        branch[u].append(v)
        unionFind.unite(u, v)

    parents = unionFind.get_parents_list()
    cnt_vertices_list: List[Tuple[int, int]] = [
        dfs(parent, branch) for parent in parents]
    for cnt in cnt_vertices_list:
        if cnt == (0, 0):
            print(0)
            exit()
    if len(parents) == 1:
        print(cnt_vertices_list[0][0] * cnt_vertices_list[0][1] - m)
        exit()
    ans = n * (n - 1) // 2 - m
    for (a, b) in cnt_vertices_list:
        ans -= a * (a - 1) // 2
        ans -= b * (b - 1) // 2
    print(ans)


if __name__ == '__main__':
    main()
