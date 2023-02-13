from typing import List, Dict

if __name__ == '__main__':
    n, m = map(int, input().split())
    numbers_list: List[List[int]] = []
    for _ in range(m):
        _ = int(input())
        numbers_list.append(list(map(int, input().split())))

    ans = 0

    for i in range(2 ** m):
        set_index = []
        for j in range(m):
            if (i >> j) & 1:
                set_index.append(j)
        if set_index == []:
            continue
        numbers_dic: Dict[int, bool] = {key: False for key in range(1, n + 1)}
        for index in set_index:
            for num in numbers_list[index]:
                numbers_dic[num] = True

        if list(set(numbers_dic.values())) == [True]:
            ans += 1

    print(ans)
