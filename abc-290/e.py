if __name__ == '__main__':
    n = int(input())
    ans = n * (n - 1) // 2
    num_and_count_dic = {}
    for num in list(map(int, input().split())):
        if num in num_and_count_dic.keys():
            num_and_count_dic[num] += 1
        else:
            num_and_count_dic[num] = 1

    for _, cnt in num_and_count_dic.items():
        ans -= cnt * (cnt - 1) // 2

    print(ans)


# mistake