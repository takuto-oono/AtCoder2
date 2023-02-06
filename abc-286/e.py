from collections import deque
from typing import List, Tuple


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    s_list: List[str] = [input() for _ in range(n)]
    q = int(input())
    branch: List[List[int]] = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if s_list[i][j] == 'Y':
                branch[i].append(j)

    ans_list: List[List[Tuple[int, int]]] = [
        [(-1, -1) for _ in range(n)] for _ in range(n)]

    def bfs(start: int) -> None:
        todo_list: deque[Tuple[int, int]] = deque(
            [(t, start) for t in branch[start]])
        number_of_flights = [-1 for _ in range(n)]
        value_of_souvenirs = [-1 for _ in range(n)]
        number_of_flights[start] = 0
        value_of_souvenirs[start] = a_list[start]

        while len(todo_list) > 0:
            now_city, before_city = todo_list.popleft()
            if number_of_flights[now_city] == -1:
                number_of_flights[now_city] = number_of_flights[before_city] + 1
                value_of_souvenirs[now_city] = a_list[now_city] + \
                    value_of_souvenirs[before_city]
                for next_city in branch[now_city]:
                    todo_list.append((next_city, now_city))
            else:
                if number_of_flights[now_city] == number_of_flights[before_city] + 1:
                    value_of_souvenirs[now_city] = max(
                        value_of_souvenirs[now_city], value_of_souvenirs[before_city] + a_list[now_city])

        for i in range(n):
            ans_list[start][i] = (number_of_flights[i], value_of_souvenirs[i])

    for s in range(n):
        bfs(s)

    for _ in range(q):
        u, v = map(int, input().split())
        (flights, values) = ans_list[u - 1][v - 1]
        if flights == -1:
            print('Impossible')
        else:
            print(flights, values)


if __name__ == '__main__':
    main()
