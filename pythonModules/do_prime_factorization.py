import math
from typing import Dict


def do_prime_factorization(x: int) -> Dict[int, int]:
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
