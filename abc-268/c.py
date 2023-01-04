from typing import List, Dict
import collections

N = int(input())
P_LIST = list(map(int, input().split()))


def create_list_dif_index_and_value() -> List[int]:
    return [p - i for i, p in enumerate(P_LIST)]


def get_value_in_dict(key: int, dic: Dict[int, int]) -> int:
    key %= N
    if key in dic:
        return dic[key]
    return 0


def create_value_counters(li: List[int]) -> Dict[int, int]:
    res = {}
    for v in li:
        v %= N
        if v in res:
            res[v] += 1
        else:
            res[v] = 1
    return res


def find_ans(dif_index_and_values: List[int]) -> int:
    ans = 0
    value_counters = create_value_counters(create_list_dif_index_and_value())

    for i in range(N):
        x = get_value_in_dict(i, value_counters) + get_value_in_dict(i - 1,
                                                                     value_counters) + get_value_in_dict(i + 1, value_counters)
        ans = max(x, ans)
    return ans


def main():
    print(find_ans(create_list_dif_index_and_value()))


if __name__ == '__main__':
    main()
