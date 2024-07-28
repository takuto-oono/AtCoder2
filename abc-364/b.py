from typing import List, Tuple


def main():
    h, w = map(int, input().split())
    sy, sx = map(int, input().split())
    sy, sx = sy - 1, sx - 1

    c: List[List[str]] = [list(input()) for _ in range(h)]

    for x in list(input()):
        sy, sx = move(c, sy, sx, x)

    print(sy + 1, sx + 1)


def move(c: List[List[str]], sy: int, sx: int, action: str) -> Tuple[int, int]:
    match action:
        case 'U':
            if sy == 0 or c[sy - 1][sx] == '#':
                return sy, sx
            return sy - 1, sx
        case 'D':
            if sy == len(c) - 1 or c[sy + 1][sx] == '#':
                return sy, sx
            return sy + 1, sx
        case 'L':
            if sx == 0 or c[sy][sx - 1] == '#':
                return sy, sx
            return sy, sx - 1
        case 'R':
            if sx == len(c[0]) - 1 or c[sy][sx + 1] == '#':
                return sy, sx
            return sy, sx + 1
        case _:
            return sy, sx


if __name__ == '__main__':
    main()
