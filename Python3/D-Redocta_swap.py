import itertools
from typing import List, Dict, Generator


def all_pattern() -> List[str]:
    chars = list('atcoder')
    return list(itertools.permutations(chars, len(chars)))


def init_dic() -> Dict[str, int]:
    atcoder_dic = {}
    for char_list in all_pattern():
        atcoder_dic[''.join(char_list)] = -1
    atcoder_dic['atcoder'] = 0
    return atcoder_dic


def exchange_char_by_index(chars: str, index: int) -> str:
    if index + 1 >= len(chars) or index < 0:
        print('index error')
        return chars
    return chars[:index] + chars[index + 1] + chars[index] + chars[index + 2:]


def create_str_list_one_operate(chars: str) -> Generator[str, None, None]:
    for i in range(len(chars) - 1):
        yield exchange_char_by_index(chars, i)


def count_exchange_all_pattern() -> Dict[str, int]:
    atcoder_dic = init_dic()
    todo = ['atcoder']
    cnt = 0
    while len(todo) != 0:
        new_todo = []
        for t in todo:
            for new_t in create_str_list_one_operate(t):
                if atcoder_dic[new_t] == - 1:
                    atcoder_dic[new_t] = cnt + 1
                    new_todo.append(new_t)
        todo = [t for t in new_todo]
        cnt += 1
    return atcoder_dic


def main():
    s = input()
    atcoder_dic = count_exchange_all_pattern()
    print(atcoder_dic[s])


if __name__ == '__main__':
    main()
