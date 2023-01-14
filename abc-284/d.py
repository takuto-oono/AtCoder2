from typing import List, Tuple
import math


class ABC284D:
    def __init__(self) -> None:
        self.t = int(input())
        self.test_cases = [int(input()) for _ in range(self.t)]
        self.prime_number_list = self.create_prime_number_list()

    def create_prime_number_list(self) -> List[int]:
        n = 3 * 10 ** 6
        is_prime_numbers = {i: True for i in range(n + 1)}
        is_prime_numbers[0], is_prime_numbers[1] = False, False
        for i in range(2, int(math.sqrt(n)) + 1):
            if is_prime_numbers[i]:
                for j in range(2 * i, n + 1, i):
                    is_prime_numbers[j] = False
        return [number for number, bool in is_prime_numbers.items() if bool]

    def calc_p_and_q(self, n: int, prime: int) -> Tuple[int, int]:
        if n % (prime ** 2) == 0:
            return (prime, n // (prime ** 2))
        return (int(math.sqrt(n // prime)), prime)

    def find_answers(self) -> List[Tuple[int, int]]:
        answers: List[Tuple[int, int]] = [(0, 0) for _ in range(self.t)]
        cnt_done_testcase = 0
        for prime in self.prime_number_list:
            for i, n in enumerate(self.test_cases):
                if cnt_done_testcase >= self.t:
                    break

                if n % prime == 0 and answers[i] == (0, 0):
                    answers[i] = self.calc_p_and_q(n, prime)
                    cnt_done_testcase += 1

        return answers

    def print_ans(self) -> None:
        for ans in self.find_answers():
            print(str(ans[0]) + ' ' + str(ans[1]))


if __name__ == '__main__':
    ABC284D().print_ans()
