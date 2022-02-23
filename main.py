from collections import Counter

text = "adafg ad"
st = 'adc '


def solution(text, st: str):
    dict = Counter(st)
    set_st =set(st)
    if st == "":
        return st == text
    for i in text:
        if i in set_st:
            dict[i] -= 1
            if dict[i] < 0:
                dict = Counter(st)
                continue
        else:
            dict = Counter(st)
        print(dict)
    return sum(dict.values()) == 0


if __name__ == "__main__":
    print(solution(text, st))
