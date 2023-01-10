from typing import List, Tuple
from collections import deque


class ABC272D:
    def __init__(self) -> None:
        self.n, self.m = map(int, input().split())
        self.dirs: List[Tuple[int, int]] = []
        self.ans = [[-1 for _ in range(self.n)] for _ in range(self.n)]

    def append_dirs(self, y: int, x: int) -> None:
        append_list = [(y, x), (y, -x), (-y, x), (-y, -x)]
        for t in append_list:
            self.dirs.append(t)

    def enumerate_all_dirs(self) -> None:
        for i in range(self.n + 1):
            for j in range(self.n + 1):
                if i ** 2 + j ** 2 == self.m:
                    self.append_dirs(i, j)

    def bfs(self) -> None:
        self.enumerate_all_dirs()
        self.ans[0][0] = 0
        todo_list: deque[Tuple[int, int]] = deque([(0, 0)])

        while len(todo_list) > 0:
            (y, x) = todo_list.popleft()
            for (dir_y, dir_x) in self.dirs:
                next_y, next_x = y + dir_y, x + dir_x
                if not (0 <= next_y < self.n and 0 <= next_x < self.n):
                    continue
                if self.ans[next_y][next_x] >= 0:
                    continue
                self.ans[next_y][next_x] = self.ans[y][x] + 1
                todo_list.append((next_y, next_x))

    def print_ans(self) -> None:
        for nums in self.ans:
            print(' '.join(str(num) for num in nums))


if __name__ == '__main__':
    abc272c = ABC272D()
    abc272c.bfs()
    abc272c.print_ans()
