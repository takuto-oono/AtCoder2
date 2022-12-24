from typing import List


def judge_solving_all_problems(s_list_a: List[str], s_list_b: List[str]) -> bool:
    for i in range(min(len(s_list_a), len(s_list_b))):
        if not (s_list_a[i] == 'o' or s_list_b[i] == 'o'):
            return False
    return True


def main():
    n, m = map(int, input().split())
    s_list = [list(input()) for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if judge_solving_all_problems(s_list[i], s_list[j]):
                ans += 1
    print(ans)


if __name__ == '__main__':
    main()
