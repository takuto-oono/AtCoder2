from typing import List, Tuple


def main():
    n, x = map(int, input().split())
    ab_list: List[Tuple[int, int]] = []
    for _ in range(n):
        a, b = map(int, input().split())
        ab_list.append((a, b))

    dp_list: List[List[bool]] = [
        [False for _ in range(x + 1)] for _ in range(n + 1)]
    dp_list[0][0] = True

    for i in range(n):
        (a, b) = ab_list[i]
        for j in range(x + 1):
            if not dp_list[i][j]:
                continue

            for cnt in range(b + 1):
                new_cnt = j + a * cnt
                if new_cnt > x:
                    break
                dp_list[i + 1][new_cnt] = True

    if dp_list[n][x]:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
