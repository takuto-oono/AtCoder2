from typing import List, Tuple, Dict


class ABC277D:
    def __init__(self) -> None:
        self.n, self.m = map(int, input().split())
        self.a_list = sorted(list(map(int, input().split())))
        self.contain_number_list = sorted(list(set(self.a_list)))
        self.consecutive_intervals: List[tuple[int,
                                               int]] = self.find_consecutive_intervals()
        self.a_dic_number_and_count = self.create_a_dic_number_and_count()

    def find_consecutive_intervals(self) -> List[Tuple[int, int]]:
        result: List[Tuple[int, int]] = []
        begin, end = -1, -1
        for i in range(len(self.contain_number_list) - 1):
            if i == len(self.contain_number_list) - 2:
                if begin == -1:
                    if self.contain_number_list[i] + 1 == self.contain_number_list[i + 1]:
                        result.append((i, i + 1))
                else:
                    if self.contain_number_list[i] + 1 == self.contain_number_list[i + 1]:
                        end = i + 1
                    
                    result.append((begin, end))
                continue

            if begin == -1:
                if self.contain_number_list[i] + 1 == self.contain_number_list[i + 1]:
                    begin, end = i, i + 1
            else:
                if self.contain_number_list[i] + 1 == self.contain_number_list[i + 1]:
                    end = i + 1
                else:
                    result.append((begin, end))
                    begin, end = -1, -1

        if self.contain_number_list[0] == 0 and self.contain_number_list[-1] == self.m - 1:
            x1, x2 = result[0]
            y1, y2 = result[-1]
            if x1 == 0 and y2 == len(self.contain_number_list) - 1:
                result.append((y1, x2))
            elif x1 == 0:
                result.append((len(self.contain_number_list) - 1, x2))
            elif y2 == len(self.contain_number_list) - 1:
                result.append((y1, 0))
            else:
                result.append((len(self.contain_number_list) - 1, 0))

        return result

    def create_a_dic_number_and_count(self) -> Dict[int, int]:
        result: Dict[int, int] = {}
        for a in self.a_list:
            if a in result:
                result[a] += 1
            else:
                result[a] = 1
        return result

    def find_ans(self) -> int:
        if len(self.contain_number_list) == 1:
            return 0
        
        x = 0
        for k, v in self.a_dic_number_and_count.items():
            x = max(x, k * v)
        
        for (begin, end) in self.consecutive_intervals:
            tmp = 0
            if begin < end:
                keys = [self.contain_number_list[index]
                        for index in range(begin, end + 1)]
            else:
                keys = [self.contain_number_list[index] for index in range(begin, len(
                    self.contain_number_list))] + [self.contain_number_list[index] for index in range(end + 1)]
            for key in keys:
                tmp += key * self.a_dic_number_and_count[key]
            x = max(tmp, x)
        return sum(self.a_list) - x


if __name__ == '__main__':
    print(ABC277D().find_ans())
