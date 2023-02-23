if __name__ == '__main__':
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

    ans = 0
    for b in b_list:
        ans += a_list[b - 1]
    print(ans)
