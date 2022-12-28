def main():
    _, init_num = int(input()), 0
    a_dic = {i: a for i, a in enumerate(list(map(int, input().split())))}
    for _ in range(int(input())):
        query = list(map(int, input().split()))
        if query[0] == 1:
            init_num, a_dic = query[1], {}
        if query[0] == 2:
            try:
                a_dic[query[1] - 1] += query[2]
            except KeyError:
                a_dic[query[1] - 1] = query[2] + init_num
        if query[0] == 3:
            try:
                print(a_dic[query[1] - 1])
            except KeyError:
                print(init_num)


if __name__ == '__main__':
    main()
