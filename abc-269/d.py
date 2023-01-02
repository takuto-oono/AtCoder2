N = int(input())
Coordinates = {i: list(map(int, input().split())) for i in range(N)}


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


def is_next(a: int, b: int) -> bool:
    ax, ay, bx, by = Coordinates[a][0], Coordinates[a][1], Coordinates[b][0], Coordinates[b][1]
    candidates = [
        (bx, by + 1),
        (bx, by - 1),
        (bx + 1, by),
        (bx + 1, by + 1),
        (bx - 1, by),
        (bx - 1, by - 1),
    ]
    return (ax, ay) in candidates



def main():
    union_find = UnionFind(N)
    for i in range(N):
        for j in range(i + 1, N):
            if is_next(i, j):
                union_find.unite(i, j)
    print(union_find.get_parents_count())


if __name__ == '__main__':
    main()
