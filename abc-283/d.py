from typing import List
from collections import deque

class ABC283D:
    def __init__(self) -> None:
        self.s = list(input())
        self.is_ball_alpha = [False for _ in range(26)]

    def edit_is_ball_alpha(self, chr: str, flag: bool) -> bool:
        num = ord(chr) - ord('a')
        if flag:
            if self.is_ball_alpha[num]:
                return False
            else:
                self.is_ball_alpha[num] = True
                return True
        self.is_ball_alpha[num] = False
        return True

    def process_when_close_bracket(self, i: int) -> None:
        cnt_open_bracket, cnt_close_bracket = 0, 1
        j = i - 1
        while cnt_open_bracket != cnt_close_bracket:
            if self.s[j] == '(':
                cnt_open_bracket += 1
            elif self.s[j] == ')':
                cnt_close_bracket += 1
            else:
                self.edit_is_ball_alpha(self.s[j], False)
            j -= 1

    def process_main(self) -> bool:
        cnt_open_bracket, cnt_close_bracket = 0, 0
        take_out_memo: deque[List[str]] = deque()
        for chr in self.s:
            if chr == '(':
                cnt_open_bracket += 1
                take_out_memo.appendleft([])
                
            elif chr == ")":
                cnt_close_bracket += 1
                for c in take_out_memo.popleft():
                    self.edit_is_ball_alpha(c, False)
            else:
                if not self.edit_is_ball_alpha(chr, True):
                    return False
                if cnt_open_bracket != cnt_close_bracket:
                    take_out_memo[0].append(chr)
                    
        return True
                    

if __name__ == '__main__':
    if ABC283D().process_main():
        print('Yes')
    else:
        print('No')
