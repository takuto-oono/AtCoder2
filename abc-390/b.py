def main():
    n = int(input())
    a_list = list(map(int, input().split()))

    if n < 3:
        print("Yes")
        return

    for i in range(0, n - 2):
        if a_list[i+1] ** 2 != a_list[i] * a_list[i+2]:
            print("No")
            return

    print("Yes")


if __name__ == '__main__':
    main()
