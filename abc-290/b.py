if __name__ == '__main__':
    n, k = map(int, input().split())
    s_list = list(input())
    ans = ['x' for _ in range(n)]
    cnt = 0
    for i, s in enumerate(s_list):
        if cnt >= k:
            break
        if s == 'o':
            ans[i] = 'o'
            cnt += 1
    print(''.join(ans))
