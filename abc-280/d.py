from typing import Dict
import math


class ABC280D:
    def __init__(self) -> None:
        self.k = int(input())

    def do_prime_factorization(self, x: int) -> Dict[int, int]:
        result = {}
        tmp = x
        for i in range(2, int(math.sqrt(x)) + 1):
            if tmp % i == 0:
                cnt = 0
                while tmp % i == 0:
                    cnt += 1
                    tmp //= i
                result[i] = cnt
        if tmp != 1:
            result[tmp] = 1

        if result == {}:
            result[x] = 1

        return result

    def find_ans(self) -> None:
        ans = 1
        for k, v in self.do_prime_factorization(self.k).items():
            cnt = 0
            for i in range(1, 10 ** 7):
                tmp = k * i
                while tmp % k == 0:
                    cnt += 1
                    tmp //= k

                if cnt >= v:
                    ans = max(ans, k * i)
                    break

        print(ans)


if __name__ == '__main__':
    ABC280D().find_ans()
