from typing import List, Dict


def lcp(s_list: str, t_list: str) -> int:
    i = 0
    while i < min(len(s_list), len(t_list)):
        if s_list[i] != t_list[i]:
            break
        i += 1
    return i


def main():
    n = int(input())
    s_list: List[str] = [input() for _ in range(n)]
    s_dic: Dict[str, List[int]] = {}
    for i, s in enumerate(s_list):
        if s in s_dic.keys():
            s_dic[s].append(i)
        else:
            s_dic[s] = [i]
            
    s_list.sort()
    ans_list = [0 for _ in range(n)]
    
    for i in range(n):
        if ans_list[s_dic[s_list[i]][0]] != 0:
            continue

        ans = 0
        if i == 0:
            ans = lcp(s_list[i], s_list[i + 1])

        elif i == n - 1:
            ans = lcp(s_list[i], s_list[i - 1])

        else:
            ans = max(
                lcp(s_list[i], s_list[i + 1]),
                lcp(s_list[i], s_list[i - 1])
            )
        for index in s_dic[s_list[i]]:
            ans_list[index] = ans

    for ans in ans_list:
        print(ans)


if __name__ == '__main__':
    main()
