from typing import List


def main():
    n = int(input())
    s_list: List[List[str]] = [list(input()) for _ in range(n)]

    t_list: List[List[str]] = [['' for _ in range(n)] for _ in range(max(len(s) for s in s_list))]

    for i, s in enumerate(s_list):
        for j, c in enumerate(s):
            t_list[j][i] = c

    for i, t in enumerate(t_list):
        is_asterisk = False
        for j, c in enumerate(t):
            if c == '':
                if is_asterisk:
                    t_list[i][j] = '*'
            else:
                is_asterisk = True

    for t in t_list:
        print(''.join(reversed(t)))


if __name__ == '__main__':
    main()
