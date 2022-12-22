def main():
    k = int(input())
    ans = ''
    x = ord('A')
    for _ in range(k):
        ans += chr(x)
        x += 1
    print(ans)


if __name__ == '__main__':
    main()
