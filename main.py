from collections import Counter

text = "adc  afg adc"
st = 'adc  '


def solution(text, st: str):
    if len(st) > len(text):
        return False
    dict = Counter(st)
    start_dict = Counter(st)
    set_st = set(st)
    if st == "":
        return st == text
    for i in text:
        if i in set_st:
            dict[i] -= 1
            if dict[i] < 0:
                dict = start_dict
                continue
        else:
            dict = start_dict
        print(dict)
    return sum(dict.values()) == 0


if __name__ == "__main__":
    print(solution(text, st))
