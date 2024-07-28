def main():
    C().process()


class C:
    def __init__(self):
        self.n, self.x, self.y = map(int, input().split())
        self.a_list = list(map(int, input().split()))
        self.b_list = list(map(int, input().split()))

    def process(self) -> None:
        print(self.eat())

    def eat(self) -> int:
        sum_a, sum_b = 0, 0
        a_list, b_list = sorted(self.a_list, reverse=True), sorted(self.b_list, reverse=True)

        for i in range(self.n):
            sum_a += a_list[i]
            sum_b += b_list[i]

            if sum_a > self.x or sum_b > self.y:
                return i + 1

        return self.n


if __name__ == '__main__':
    main()
