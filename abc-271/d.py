from typing import List


class ABC271D:
    def __init__(self) -> None:
        self.n, self.s = map(int, input().split())
        self.ab_list = [list(map(int, input().split())) for _ in range(self.n)]
        self.dp_list = [[False for _ in range(
            self.s + 1)] for _ in range(self.n)]

    def dp(self) -> bool:
        for i in range(self.n):
            if i == 0:
                a, b = self.ab_list[i][0], self.ab_list[i][1]
                if a <= self.s:
                    self.dp_list[i][a] = True
                if b <= self.s:
                    self.dp_list[i][b] = True
                continue
            for j in range(self.s + 1):
                if self.dp_list[i - 1][j]:
                    a, b = self.ab_list[i][0], self.ab_list[i][1]
                    if j + a <= self.s:
                        self.dp_list[i][j + a] = True
                    if j + b <= self.s:
                        self.dp_list[i][j + b] = True

        return self.dp_list[self.n - 1][self.s]

    def create_sample_pattern_list(self) -> List[str]:
        tmp = self.s
        result: List[str] = []
        for i in reversed(range(self.n)):
            [a, b] = self.ab_list[i]
            if i == 0:
                if tmp == a:
                    result.append('H')
                elif tmp == b:
                    result.append('T')
            else:
                if tmp - a >= 0 and tmp - b >= 0:
                    if self.dp_list[i - 1][tmp - a]:
                        tmp -= a
                        result.append('H')
                    elif self.dp_list[i - 1][tmp - b]:
                        tmp -= b
                        result.append('T')
                elif tmp - a >= 0:
                    if self.dp_list[i - 1][tmp - a]:
                        tmp -= a
                        result.append('H')
                elif tmp - b >= 0:
                    if self.dp_list[i - 1][tmp - b]:
                        tmp -= b
                        result.append('T')

        result.reverse()
        return result

    def find_ans(self):
        if self.dp():
            print('Yes')
            print(''.join(self.create_sample_pattern_list()))
        else:
            print('No')


if __name__ == '__main__':
    ABC271D().find_ans()
