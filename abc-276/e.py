from typing import List, Tuple
from collections import deque


class ABC276E:
    def __init__(self) -> None:
        self.h, self.w = map(int, input().split())
        self.c_map = [list(input()) for _ in range(self.h)]
        self.start_coordinate = self.find_start_coordinate()
        self.branch: List[List[List[Tuple[int, int]]]] = self.create_branch()

    def find_start_coordinate(self) -> Tuple[int, int]:
        result = (-1, -1)
        for y in range(self.h):
            for x in range(self.w):
                if self.c_map[y][x] == 'S':
                    self.c_map[y][x] = '.'
                    result = (y, x)
                    break
        return result

    def create_branch(self) -> List[List[List[Tuple[int, int]]]]:
        branch: List[List[List[Tuple[int, int]]]] = [[[]
                                                      for _ in range(self.w)] for _ in range(self.h)]
        for y in range(self.h):
            for x in range(self.w):
                next_path_list: List[Tuple[int, int]] = []
                if self.c_map[y][x] == '#':
                    continue
                if y - 1 >= 0:
                    if self.c_map[y-1][x] == '.':
                        next_path_list.append((y-1, x))
                if y + 1 < self.h:
                    if self.c_map[y+1][x] == '.':
                        next_path_list.append((y+1, x))
                if x - 1 >= 0:
                    if self.c_map[y][x-1] == '.':
                        next_path_list.append((y, x-1))
                if x + 1 < self.w:
                    if self.c_map[y][x+1] == '.':
                        next_path_list.append((y, x+1))
                branch[y][x] = next_path_list

        return branch

    def dfs(self) -> bool:
        is_visit: List[List[bool]] = [
            [False for _ in range(self.w)] for _ in range(self.h)]
        cnt_how_many_times = [[-1 for _ in range(self.w)] for _ in range(self.h)]
        todo: deque[Tuple[int, int, int]] = deque(
            [(self.start_coordinate[0], self.start_coordinate[1], 0)])
        while len(todo) > 0:
            now_coordinate: Tuple[int, int, int] = todo.popleft()
            y, x, cnt = now_coordinate[0], now_coordinate[1], now_coordinate[2]
            if is_visit[y][x]:
                continue
            is_visit[y][x] = True
            cnt_how_many_times[y][x] = cnt
            for next_coordinate in self.branch[y][x]:
                if not is_visit[next_coordinate[0]][next_coordinate[1]]:
                    todo.appendleft((next_coordinate[0], next_coordinate[1], cnt + 1))
        
        y, x = self.start_coordinate[0], self.start_coordinate[1]
        if y - 1 >= 0:
            if cnt_how_many_times[y-1][x] >= 3:
                return True
        if y + 1 < self.h:
            if cnt_how_many_times[y+1][x] >= 3:
                return True
        if x - 1 >= 0:
            if cnt_how_many_times[y][x - 1] >= 3:
                return True
        if x + 1 < self.w:
            if cnt_how_many_times[y][x+1] >= 3:
                return True
        return False


if __name__ == '__main__':
    if ABC276E().dfs():
        print('Yes')
    else:
        print('No')
