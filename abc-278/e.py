from typing import Dict
import sys


class ABC278E:
    def __init__(self) -> None:
        self.h, self.w, self.n, self.y, self.x = map(int, input().split())
        self.a_list = [list(map(int, input().split())) for _ in range(self.h)]
        self.ans_list = [[0 for _ in range(self.w - self.x + 1)]
                         for _ in range(self.h - self.y + 1)]
        self.number_and_counter = self.create_number_and_counter_dic()

    def create_number_and_counter_dic(self) -> Dict[int, int]:
        result = {key: 0 for key in range(1, self.n + 1)}
        for i in range(self.h):
            for j in range(self.w):
                result[self.a_list[i][j]] += 1
        return result

    def create_black_out_number_and_counter_dic(self, i: int, j: int) -> Dict[int, int]:
        result = {key: 0 for key in range(1, self.n + 1)}
        for li in self.a_list[i:i+self.y]:
            for a in li[j:j+self.x]:
                result[a] += 1

        return result

    def find_answers(self) -> None:
        black_out_number_and_counter = self.create_black_out_number_and_counter_dic(
            0, 0)

        is_done_list = [[False for _ in range(self.w - self.x + 1)]
                        for _ in range(self.h - self.y + 1)]

        def find_ans(y: int, x: int, black_out_number_and_counter: Dict[int, int]) -> None:
            is_done_list[y][x] = True
            ans = 0
            for key in range(1, self.n + 1):
                if self.number_and_counter[key] - black_out_number_and_counter[key] > 0:
                    ans += 1
            self.ans_list[y][x] = ans
            if y + 1 < self.h - self.y + 1:
                if not is_done_list[y+1][x]:
                    new_dic = black_out_number_and_counter.copy()
                    for a in self.a_list[y][x: x + self.x]:
                        new_dic[a] -= 1
                    for a in self.a_list[y + self.y][x: x + self.x]:
                        new_dic[a] += 1
                    find_ans(y + 1, x, new_dic)
            if x + 1 < self.w - self.x + 1:
                if not is_done_list[y][x + 1]:
                    new_dic = black_out_number_and_counter.copy()
                    for a in [l[x] for l in self.a_list[y:y+self.y]]:
                        new_dic[a] -= 1
                    for a in [l[x + self.x] for l in self.a_list[y:y + self.y]]:
                        new_dic[a] += 1
                    find_ans(y, x + 1, new_dic)

        find_ans(0, 0, black_out_number_and_counter)

    def print_answers(self) -> None:
        for l in self.ans_list:
            print(' '.join([str(ans) for ans in l]))


if __name__ == '__main__':
    sys.setrecursionlimit(10 ** 9)
    abc278e = ABC278E()
    abc278e.find_answers()
    abc278e.print_answers()
