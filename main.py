from collections import Counter

text = "adafg ad"
st = 'ad'


def solution(text, st: str):
    dict = Counter(st)
    if st == "":
        return st == text
    for i in text:
        if i in set(st):
            dict[i] -= 1
            if dict[i] < 0:
                dict = Counter(st)
                continue
        else:
            dict = Counter(st)
        print(dict)
        if sum(dict.values()) == 0:
            return True
            break
    return False


if __name__ == "__main__":
    print(solution(text, st))
