from typing import Dict, List


def main():
    nums: Dict[int, int] = {i: 0 for i in range(1, 10 ** 6 + 1)}
    ans = 0
    for _ in range(int(input())):
        query: List[int] = list(map(int, input().split()))
        if query[0] == 1:
            x = query[1]
            if nums[x] == 0:
                ans += 1
            nums[x] += 1

        elif query[0] == 2:
            x = query[1]
            if nums[x] == 1:
                ans -= 1
            nums[x] -= 1

        else:
            print(ans)


if __name__ == '__main__':
    main()
