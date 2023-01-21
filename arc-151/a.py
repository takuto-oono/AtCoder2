from typing import List


class ARC151A:
    def __init__(self) -> None:
        self.n = int(input())
        self.s = [int(str) for str in list(input())]
        self.t = [int(str) for str in list(input())]
        self.different_litters_index_list = [
            index for index in range(self.n) if self.s[index] != self.t[index]]

    def exist_ans(self) -> bool:
        return len(self.different_litters_index_list) % 2 == 0

    def find_ans(self) -> List[int]:
        result = [0 for _ in range(self.n)]
        cnt_s, cnt_t = 0, 0
        for index in self.different_litters_index_list:
            if self.s[index] == 0:
                cnt_s += 1
            if self.t[index] == 0:
                cnt_t += 1

        if cnt_s == cnt_t:
            return result

        cnt_exchange = 0
        if cnt_s > cnt_t:
            for index in reversed(self.different_litters_index_list):
                if cnt_exchange == (cnt_s - cnt_t) // 2:
                    break
                if self.s[index] == 0:
                    result[index] = 1
                    cnt_exchange += 1

        if cnt_s < cnt_t:
            for index in reversed(self.different_litters_index_list):
                if cnt_exchange == (cnt_t - cnt_s) // 2:
                    break
                if self.t[index] == 0:
                    result[index] = 1
                    cnt_exchange += 1
        return result

    def print_ans(self) -> None:
        print(''.join([str(num) for num in self.find_ans()]))


if __name__ == '__main__':
    arc151a = ARC151A()
    if arc151a.exist_ans():
        arc151a.print_ans()
    else:
        print(-1)
