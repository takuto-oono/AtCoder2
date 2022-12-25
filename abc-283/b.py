from typing import List


def process_1(a_list: List[int], k: int, x: int) -> List[int]:
    a_list[k - 1] = x
    return a_list


def process_2(a_list: List[int], k: int) -> None:
    print(a_list[k-1])


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    q = int(input())
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            a_list = process_1(a_list, query[1], query[2])
        elif query[0] == 2:
            process_2(a_list, query[1])


if __name__ == '__main__':
    main()
