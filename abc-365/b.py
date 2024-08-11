def main():
    _ = int(input())
    a_list = list(map(int, input().split()))
    a_max = max(a_list)
    ans = 0
    a_second_max = 0
    for i, a in enumerate(a_list):
        if a == a_max:
            continue
        if a > a_second_max:
            a_second_max = a
            ans = i + 1

    print(ans)


if __name__ == '__main__':
    main()
