from typing import List, Generator, Tuple
import sys


class ABC267D:
    def __init__(self) -> None:
        self.n, self.m = map(int, input().split())
        self.a_list = list(map(int, input().split()))

    def dp(self) -> int:
        dp_list = [
            [-sys.maxsize for _ in range(self.n + 1)] for _ in range(self.n + 1)]
        dp_list[0][0] = 0
        for i in range(1, self.n + 1):
            for j in range(i + 1):
                if j == 0:
                    dp_list[i][j] = 0
                    continue
                
                dp_list[i][j] = max(
                    dp_list[i - 1][j], dp_list[i - 1][j - 1] + self.a_list[i - 1] * j)
        return dp_list[self.n][self.m]


if __name__ == '__main__':
    print(ABC267D().dp())
