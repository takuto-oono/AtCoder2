import sys
sys.setrecursionlimit(10 ** 9)

if __name__ == '__main__':
    n = int(input())
    climb_steps_list = list(map(int, input().split()))
    m = int(input())
    traps_steps = list(map(int, input().split()))
    is_trap_dic = {step: False for step in range(10 ** 5 + 1)}
    for trap_steps in traps_steps:
        is_trap_dic[trap_steps] = True
    x = int(input())
    is_visit_dic = {step: False for step in range(10 ** 5 + 1)}

    def dfs(now_step) -> bool:
        if now_step > x:
            return False
        if now_step == x:
            return True
        is_visit_dic[now_step] = True
        if is_trap_dic[now_step]:
            return False

        for climb_steps in climb_steps_list:
            if now_step + climb_steps > x:
                continue
            if is_visit_dic[now_step + climb_steps]:
                continue
            if dfs(now_step + climb_steps):
                return True
        return False

    if dfs(0):
        print('Yes')
    else:
        print('No')
