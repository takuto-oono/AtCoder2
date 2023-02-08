from typing import Tuple, List, Dict
import bisect


def main():
    h, w, rs, cs = map(int, input().split())
    ny, nx = rs - 1, cs - 1
    n = int(input())
    squares: List[Tuple[int, int]] = []
    for _ in range(n):
        r, c = map(int, input().split())
        squares.append((r - 1, c - 1))
    q = int(input())

    squares_y_dic: Dict[int, List[int]] = {}
    squares_x_dic: Dict[int, List[int]] = {}

    for r, c in squares:
        if r in squares_y_dic.keys():
            bisect.insort(squares_y_dic[r], c)
        else:
            squares_y_dic[r] = [c]

        if c in squares_x_dic.keys():
            bisect.insort(squares_x_dic[c], r)
        else:
            squares_x_dic[c] = [r]

    for _ in range(q):
        d, l = input().split()
        l = int(l)
        if d == 'U':
            candidate_y = max(ny - l, 0)
            if nx not in squares_x_dic.keys():
                ny = candidate_y
                print(ny + 1, nx + 1)
                continue
            index_ny = bisect.bisect_left(squares_x_dic[nx], ny)
            index_candidate_y = bisect.bisect_left(
                squares_x_dic[nx], candidate_y)
            if index_ny == index_candidate_y:
                ny = candidate_y
            else:
                ny = squares_x_dic[nx][index_ny - 1] + 1

        if d == 'D':
            candidate_y = min(h - 1, ny + l)
            if nx not in squares_x_dic.keys():
                ny = candidate_y
                print(ny + 1, nx + 1)
                continue
            index_ny = bisect.bisect_right(squares_x_dic[nx], ny)
            index_candidate_y = bisect.bisect_right(
                squares_x_dic[nx], candidate_y)
            if index_ny == index_candidate_y:
                ny = candidate_y
            else:
                ny = squares_x_dic[nx][index_ny] - 1

        if d == 'L':
            candidate_x = max(nx - l, 0)
            if ny not in squares_y_dic.keys():
                nx = candidate_x
                print(ny + 1, nx + 1)
                continue
            index_nx = bisect.bisect_left(squares_y_dic[ny], nx)
            index_candidate_x = bisect.bisect_left(
                squares_y_dic[ny], candidate_x)
            if index_nx == index_candidate_x:
                nx = candidate_x
            else:
                nx = squares_y_dic[ny][index_nx - 1] + 1

        if d == 'R':
            candidate_x = min(w - 1, nx + l)
            if ny not in squares_y_dic.keys():
                nx = candidate_x
                print(ny + 1, nx + 1)
                continue
            index_nx = bisect.bisect_right(squares_y_dic[ny], nx)
            index_candidate_x = bisect.bisect_right(
                squares_y_dic[ny], candidate_x)
            if index_nx == index_candidate_x:
                nx = candidate_x
            else:
                nx = squares_y_dic[ny][index_nx] - 1

        print(ny + 1, nx + 1)


if __name__ == '__main__':
    main()
