from collections import deque


def main():
    s_list = list(input())
    t_list = list(input())
    len_t = len(t_list)
    index_list_of_bad_status: deque[int] = deque([])
    ans_list = [False for _ in range(len_t + 1)]

    for x in range(len_t + 1):
        if x == 0:
            for i, t in enumerate(t_list):
                if not (s_list[i - len_t] == '?' or t == '?' or s_list[i - len_t] == t):
                    index_list_of_bad_status.append(i)

            if len(index_list_of_bad_status) == 0:
                ans_list[x] = True
            continue

        if len(index_list_of_bad_status) > 0:
            if index_list_of_bad_status[0] < x - 1:
                break

        if s_list[x - 1] == '?' or t_list[x - 1] == '?' or s_list[x - 1] == t_list[x - 1]:
            if len(index_list_of_bad_status) == 0:
                ans_list[x] = True
                continue
            
            if index_list_of_bad_status[0] == x - 1:
                index_list_of_bad_status.popleft()
                
            ans_list[x] = len(index_list_of_bad_status) == 0
            
        else:
            if len(index_list_of_bad_status) == 0:
                index_list_of_bad_status.appendleft(x - 1)
            
            if index_list_of_bad_status[0] != x - 1:
                index_list_of_bad_status.appendleft(x - 1)

    for ans in ans_list:
        if ans:
            print('Yes')
        else:
            print('No')


if __name__ == '__main__':
    main()
