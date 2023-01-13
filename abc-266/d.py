from typing import List, Dict


class ABC266D:
    def __init__(self) -> None:
        self.n = int(input())
        self.txa_dic: Dict[int, List[List[int]]] = {}
        self.t_list = [0]

        for _ in range(self.n):
            t, x, a = map(int, input().split())
            if t in self.txa_dic:
                self.txa_dic[t].append([x, a])
            else:
                self.txa_dic[t] = [[x, a]]
                self.t_list.append(t)

        self.t_list.sort()

    def find_a(self, t: int, x: int) -> int:
        for xa_list in self.txa_dic[t]:
            if xa_list[0] == x:
                return xa_list[1]
        return 0

    def dp(self) -> int:
        dp_list = [[-1 for _ in range(5)] for _ in range(len(self.t_list))]
        dp_list[0][0] = 0

        for i in range(len(self.t_list) - 1):
            now_t, next_t = self.t_list[i], self.t_list[i+1]
            a_list = [self.find_a(next_t, x) for x in range(5)]
            for x in range(5):
                if dp_list[i][x] == -1:
                    continue

                to_list = [x]

                k = 1
                while x - k >= 0 and k <= next_t - now_t:
                    to_list.append(x - k)
                    k += 1

                k = 1
                while x + k < 5 and k <= next_t - now_t:
                    to_list.append(x + k)
                    k += 1
                for to in to_list:
                    dp_list[i+1][to] = max(dp_list[i+1]
                                           [to], dp_list[i][x] + a_list[to])

        return max(dp_list[-1])


if __name__ == '__main__':
    print(ABC266D().dp())
