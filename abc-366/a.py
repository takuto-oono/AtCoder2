def main():
    n, t, a = map(int, input().split())

    m = n - t - a
    if min(t, a) + m < max(t, a):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
