def main():
    s_str = input()

    a_list, b_list, c_list = [], [], []

    for i, s in enumerate(s_str):
        if s == "A":
            a_list.append(i)
        elif s == "B":
            b_list.append(i)
        elif s == "C":
            c_list.append(i)

    ans = 0
    for a in a_list:
        for b in b_list:
            for c in c_list:
                if a < b < c and c - b == b - a:
                    ans += 1

    print(ans)


if __name__ == "__main__":
    main()
