if __name__ == '__main__':
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    nums = sorted(list(set(nums)))

    expected_num = 0
    for num in nums:
        if expected_num == k:
            break

        if num == expected_num:
            expected_num += 1
        else:
            break

    print(expected_num)
