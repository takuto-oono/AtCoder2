from typing import Dict, Tuple

Ans_Dict = {0: 1}


def f(x: int) -> int:
    if x == 0:
        return 1

    if x in Ans_Dict:
        return Ans_Dict[x]

    ans = f(x // 2) + f(x // 3)
    Ans_Dict[x] = ans
    while x % 2 != 0 and x % 3 != 0:
        Ans_Dict[x] = ans
        x += 1
    return ans


def main():
    n = int(input())
    print(f(n))


if __name__ == '__main__':
    main()
