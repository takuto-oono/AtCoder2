def main():
    a_list = list(map(int, input().split()))
    ans_list = [1, 2, 3, 4, 5]

    for i in range(4):
        j = i + 1
        c_list = a_list.copy()
        c_list[i], c_list[j] = c_list[j], c_list[i]
        if c_list == ans_list:
            print('Yes')
            return

    print('No')


if __name__ == '__main__':
    main()
