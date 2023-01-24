import itertools
from typing import List


class ABC281D:
    def __init__(self) -> None:
        self.n, self.k, self.d = map(int, input().split())
        self.a_list = list(map(int, input().split()))

    def dp(self) -> int:
        dp_list: List[List[List[int]]] = [
            [[-1 for _ in range(self.d)] for _ in range(self.k + 1)] for _ in range(self.n + 1)]
        dp_list[0][0][0] = 0
        for i in range(self.n):
            for j in range(self.k + 1):
                for l in range(self.d):
                    if dp_list[i][j][l] == -1:
                        continue

                    dp_list[i + 1][j][l] = max(dp_list[i + 1]
                                               [j][l], dp_list[i][j][l])

                    if j != self.k:
                        dp_list[i + 1][j + 1][(l + self.a_list[i]) % self.d] = max(dp_list[i + 1][j + 1][(
                            l + self.a_list[i]) % self.d], dp_list[i][j][l] + self.a_list[i])

        return dp_list[self.n][self.k][0]


if __name__ == "__main__":
    print(ABC281D().dp())
