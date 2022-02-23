from collections import Counter

text = "ddacaacgasdf addc"
st = 'adcd '


def solution(text, st: str):
    dict = Counter(st)
    count = len(st)
    set_st = set(st)
    j = 0
    if st == "":
        return st == text
    for i in text:
        if i in dict.keys():
            dict[i] -= 1
            count -= 1
            j += 1
            if dict[i] < 0:
                dict = Counter(st)
                continue
        else:
            dict = Counter(st)
            count += j
            j = 0
        print(count, dict)
        if count == 0:
            if sum(dict.values()) == 0:
                return True
    return False


if __name__ == "__main__":
    print(solution(text, st))
