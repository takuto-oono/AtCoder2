from typing import Generator, Tuple, List

N, P, Q, R = map(int, input().split())
A_LIST = list(map(int, input().split()))


def create_cumulative_sum_list() -> Generator[int, None, None]:
    res = 0
    yield res
    for a in A_LIST:
        res += a
        yield res


def find_section_a_list_sum_pqr() -> Generator[Tuple[int, int], None, None]:
    cumulative_sum_a_list = [s for s in create_cumulative_sum_list()]
    j = 0

    for i in range(N):
        while j < len(cumulative_sum_a_list):
            if cumulative_sum_a_list[j] - cumulative_sum_a_list[i] >= P + Q + R:
                break
            j += 1
        if j == len(cumulative_sum_a_list):
            break

        if cumulative_sum_a_list[j] - cumulative_sum_a_list[i] == P + Q + R:
            yield i, j


def find_sum_x_a_list(a_list: List[int], x: int) -> int:
    s = 0
    for i, v in enumerate(a_list):
        s += v
        if s == x:
            return i
        if s > x:
            return -1
    return -1


def is_exist_x_y_z_w() -> bool:
    for x, w in [sec for sec in find_section_a_list_sum_pqr()]:
        a_list_section_x_w = A_LIST[x:w]
        y = find_sum_x_a_list(a_list_section_x_w, P)
        z = find_sum_x_a_list(a_list_section_x_w[::-1], R)
        if y != -1 and z != -1:
            y += x + 1
            z = w - z - 1
            sum_y_z = 0
            for i in range(y, z):
                sum_y_z += A_LIST[i]
            if sum_y_z == Q:
                return True
    return False


def main():
    if is_exist_x_y_z_w():
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
