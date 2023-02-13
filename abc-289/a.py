if __name__ == '__main__':
    s = input()
    ans = ''
    for c in s:
        if c == '0':
            ans += '1'
        if c == '1':
            ans += '0'
    print(ans)
