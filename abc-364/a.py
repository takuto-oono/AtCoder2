def main():
    n = int(input())
    s_list = [input() for _ in range(n)]

    is_done = True
    for i in range(n - 2):
        if s_list[i] == 'sweet' and s_list[i + 1] == 'sweet':
            is_done = False
            break

    if is_done:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
