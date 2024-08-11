def main():
    C().process()


class C:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.a_list = sorted(list(map(int, input().split())))

    def process(self) -> None:
        if self.is_infinite():
            print('infinite')
            return

        print(self.binary_search())

    def calc(self, x: int) -> int:
        acc = 0
        for a in self.a_list:
            acc += min(a, x)
        return acc

    def binary_search(self) -> int:
        left = 0
        right = 10 ** 9 + 1
        while abs(right - left) > 1:
            mid = (left + right) // 2
            if self.calc(mid) > self.m:
                right = mid
            else:
                left = mid
        return left

    def is_infinite(self) -> bool:
        return sum(self.a_list) <= self.m


if __name__ == '__main__':
    main()
