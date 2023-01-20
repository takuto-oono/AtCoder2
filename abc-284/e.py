from typing import List
import sys


class ABC284E:
    def __init__(self) -> None:
        self.n, self.m = map(int, input().split())
        self.branch: List[List[int]] = self.create_branch_list()
        self.limit = 10 ** 6
        self.ans = 0
        self.is_visited = [False for _ in range(self.n)]

    def create_branch_list(self) -> List[List[int]]:
        result: List[List[int]] = [[] for _ in range(self.n)]
        for _ in range(self.m):
            u, v = map(int, input().split())
            u, v = u - 1, v - 1
            result[u].append(v)
            result[v].append(u)
        return result

    def dfs(self, x: int) -> None:
        if self.ans == self.limit:
            return
        self.is_visited[x] = True
        self.ans += 1

        for y in self.branch[x]:
            if not self.is_visited[y]:
                self.dfs(y)
        self.is_visited[x] = False

    def calc_ans(self) -> int:
        self.dfs(0)
        return self.ans


if __name__ == '__main__':
    sys.setrecursionlimit(10 ** 8)
    print(ABC284E().calc_ans())
