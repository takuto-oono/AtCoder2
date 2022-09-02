import itertools
from typing import List, Tuple, Generator


def input_matrix() -> Tuple[List[List[int]], int, int]:
    row, column = map(int, input().split())
    matrix = []
    for _ in range(row):
        matrix.append(list(map(int, input().split())))
    return matrix, row, column


def create_new_a_list(a_list: List[List[int]], row_combination: List[int], column_combination: List[int]) -> Generator[
    List[int], int, int]:
    for row in row_combination:
        new_list = []
        for column in column_combination:
            new_list.append(a_list[row][column])
        yield new_list


def is_same_a_and_b(a_list: List[List[int]], b_list: List[List[int]], a_row: int, a_column: int, b_row: int,
                    b_column) -> bool:
    row_combinations = list(itertools.combinations([i for i in range(a_row)], b_row))
    column_combinations = list(itertools.combinations([i for i in range(a_column)], b_column))

    for row_combination in row_combinations:
        for column_combination in column_combinations:
            new_a_list = [new_row for new_row in create_new_a_list(a_list, row_combination, column_combination)]
            if new_a_list == b_list:
                return True
    return False


def main():
    a_list, a_row, a_column = input_matrix()
    b_list, b_row, b_column = input_matrix()
    if is_same_a_and_b(a_list, b_list, a_row, a_column, b_row, b_column):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
