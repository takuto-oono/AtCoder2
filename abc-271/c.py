from typing import List


class ABC271C:
    def __init__(self) -> None:
        self.n = int(input())
        self.a_list = list(map(int, input().split()))
        self.a_list.sort()
        self.is_sold_or_read_list = [False for _ in range(self.n)]
        
    def order_books(self) -> List[int]:
        first_list, second_list = [], []
        for i, v in enumerate(self.a_list):
            if i == 0:
                first_list.append(v)
                continue
            if v == self.a_list[i - 1]:
                second_list.append(v)
            else:
                first_list.append(v)
        return first_list + second_list

    def find_ans(self) -> int:
        books = self.order_books()
        ans, cnt_sold_books, index = 0, 0, 0
        while ans < 10 ** 9 and index < self.n:
            if self.is_sold_or_read_list[index]:
                break
            if ans + 1 == books[index]:
                self.is_sold_or_read_list[index] = True
                index += 1

            else:
                if -cnt_sold_books - 2 < -self.n:
                    break
                if self.is_sold_or_read_list[-cnt_sold_books - 2]:
                    break
                self.is_sold_or_read_list[-cnt_sold_books - 1] = True
                self.is_sold_or_read_list[-cnt_sold_books - 2] = True
                cnt_sold_books += 2
            ans += 1
        return ans


if __name__ == '__main__':
    print(ABC271C().find_ans())
