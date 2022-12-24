def main():
    n = int(input())
    s = list(input())
    cnt_double_quotation = 0
    for i in range(n):
        if s[i] == ',':
            if cnt_double_quotation % 2 == 0:
                s[i] = '.'
        elif s[i] == '"':
            cnt_double_quotation += 1
    print(''.join(s))


if __name__ == '__main__':
    main()
