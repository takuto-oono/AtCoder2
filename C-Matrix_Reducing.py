import itertool
from typing import List, Tuple


def input_matrix() -> Tuple[List[List[int]], int, int]:
    row, column = map(int, input().split())
    matrix = []
    for _ in range(row):
        matrix.append(list(map(int, input().split())))
    return matrix, row, column


def is_same_a_and_b(a_list: List[List[int]], b_list: List[List[int]], a_row: int, a_column: int, b_row: int,
                    b_column) -> bool:
    row_combinations = list(itertool.combinations([i for i in range(a_row)], b_row))
    column_combinations = list(itertool.combinations([i for i in range(a_column)], b_column))

    //TODO 総当りでYesが出るまで繰り返す、でなければNo




def main():
    a_list, a_row, a_column = input_matrix()
    b_list, b_row, b_column = input_matrix()
