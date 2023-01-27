def calc_index(index: int, dif: int, n: int) -> int:
    return (index + dif) % n


def main():
    n, a, b = map(int, input().split())
    s_list = list(input())

    cost_list = []
    for i in range(n):
        cost = i * a
        for index in range(n // 2):
            if s_list[calc_index(index, i, n)] != s_list[calc_index(n - index - 1, i, n)]:
                cost += b
        cost_list.append(cost)
    if len(cost_list) == 0:
        print(0)
    else:
        print(min(cost_list))


if __name__ == '__main__':
    main()
