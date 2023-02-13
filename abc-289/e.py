from typing import List
from collections import deque

def main():
    n, m = map(int, input().split())
    color_list = list(map(int, input().split()))
    branch: List[List[int]] = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        branch[v].append(u)
        branch[u].append(v)
    
    todo_list: deque[int] = deque([0])
    is_visited_list = [False for _ in range(n)]
    routes: List[List[int]] = []
    route :deque[int] = deque([])
    while len(todo_list) > 0:
        now = todo_list.popleft()
        if now == n - 1:
            routes.append([p for p in route] + [now])
            continue
        if is_visited_list[now]:
            continue
        is_visited_list[now] = True
        route.append(now)
        for next in branch[now]:
            if is_visited_list[next]:
                continue
            todo_list.appendleft(next)
        

if __name__ == '__main__':
    t = int(input())
    