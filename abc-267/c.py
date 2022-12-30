from typing import List


def create_cumulative_sum_list(nums: List[int]) -> List[int]:
    res, sum = [0], 0
    for num in nums:
        sum += num
        res.append(sum)
    return res


def main():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    cumulative_sum_a_list = create_cumulative_sum_list(a_list)
    ans, x = 0, 0

    for i in range(n - m + 1):
        if i == 0:
            for j in range(m):
                x += (j + 1) * a_list[j]
                ans = x
            continue
        x -= cumulative_sum_a_list[i+m-1] - cumulative_sum_a_list[i-1]
        x += m * a_list[i+m-1]
        ans = max(ans, x)

    print(ans)


if __name__ == '__main__':
    main()
