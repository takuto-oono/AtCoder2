from typing import Dict, List
import math

N = int(input())
A_LIST = list(map(int, input().split()))


def find_greatest_common_divisor():
    g = 0
    for a in A_LIST:
        g = math.gcd(g, a)
    return g


def find_ans() -> int:
    greatest_common_divisor = find_greatest_common_divisor()
    ans = 0
    for a in A_LIST:
        a //= greatest_common_divisor

        while a % 2 == 0:
            ans += 1
            a //= 2

        while a % 3 == 0:
            ans += 1
            a //= 3

        if a != 1:
            return -1

    return ans


def main():
    print(find_ans())


if __name__ == '__main__':
    main()
