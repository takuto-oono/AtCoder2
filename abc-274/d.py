from typing import List


class ABC274D:
    def __init__(self) -> None:
        self.n, self.x, self.y = map(int, input().split())
        self.a_list = list(map(int, input().split()))

    def dp(self, numbers: List[int], final_value: int) -> bool:
        def to_index(x: int) -> int:
            return x + 10 ** 4

        dp_list = [[False for _ in range(2 * 10 ** 4 + 1)]
                   for _ in range(len(numbers))]
        dp_list[0][to_index(-numbers[0])] = True
        dp_list[0][to_index(numbers[0])] = True

        for i in range(len(numbers) - 1):
            for j in range(2 * 10 ** 4 + 1):
                if not dp_list[i][j]:
                    continue
                dp_list[i+1][j + numbers[i+1]] = True
                dp_list[i+1][j - numbers[i+1]] = True

        return dp_list[len(numbers) - 1][to_index(final_value)]

    def is_same_place(self) -> bool:
        return self.dp([num for i, num in enumerate(self.a_list) if i != 0 and i % 2 == 0], self.x - self.a_list[0]) and self.dp([num for i, num in enumerate(self.a_list) if i % 2 == 1], self.y)


if __name__ == '__main__':
    if ABC274D().is_same_place():
        print('Yes')
    else:
        print('No')
