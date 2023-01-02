import sys

sys.setrecursionlimit(10 ** 9)

N, X, Y = map(int, input().split())
Branches = [[] for _ in range(N)]
Seen = [False for _ in range(N)]
Simple_Path = []


def inputBranches() -> None:
    for _ in range(N - 1):
        u, v = map(int, input().split())
        Branches[u - 1].append(v - 1)
        Branches[v - 1].append(u - 1)


def dfs(x: int, y: int) -> bool:
    Seen[x] = True
    if y in Branches[x]:
        Simple_Path.append(y)
        return True

    for next in Branches[x]:
        if Seen[next]:
            continue

        if dfs(next, y):
            Simple_Path.append(next)
            return True
    return False


def print_simple_path() -> None:
    str_list = [str(route + 1) for route in Simple_Path]
    print(' '.join(str_list))


def main():
    inputBranches()
    dfs(Y - 1, X - 1)
    Simple_Path.append(Y - 1)
    print_simple_path()


if __name__ == '__main__':
    main()
