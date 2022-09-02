def count_is_condition(n: int) -> int:
    ans = 0
    for i in range(1, n + 1):
        x = i
        k = 2
        while k * k <= x:
            while x % (k * k) == 0:
                x //= (k * k)
            k += 1
        
        d = 1
        while x * d * d <= n:
            ans += 1
            d += 1
    return ans


def main():
    print(count_is_condition(int(input())))


if __name__ == '__main__':
    main()
