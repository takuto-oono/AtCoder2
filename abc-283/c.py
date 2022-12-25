def main():
    s = input()
    ans = len(s)
    is_before_zero = False
    for chr in s:
        if chr == '0' and is_before_zero:
            ans -= 1
            is_before_zero = False
        elif chr == '0' and (not is_before_zero):
            is_before_zero = True
        else:
            is_before_zero = False
    print(ans)


if __name__ == '__main__':
    main()
