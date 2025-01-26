def main():
    h, w = map(int, input().split())
    s_list = [input() for _ in range(h)]

    h_min, h_max, w_min, w_max = h - 1, 0, w - 1, 0

    for i in range(h):
        for j in range(w):
            s = s_list[i][j]
            if s == "#":
                h_min = min(h_min, i)
                h_max = max(h_max, i)
                w_min = min(w_min, j)
                w_max = max(w_max, j)

    ans = True
    for i in range(h):
        for j in range(w):
            if h_min <= i <= h_max and w_min <= j <= w_max:
                if s_list[i][j] == ".":
                    ans = False

    if ans:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
