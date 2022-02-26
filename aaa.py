from collections import Counter

text = "a acbfb asfgdhs"
st = 'a a'


def solution(text, st: str):
    bag = Counter(st)
    wnd = len(st)
    count = wnd

    for i, ch in enumerate(text):
        if i >= wnd and text[i - wnd] in bag:
            bag[text[i - wnd]] += 1
        if ch in bag:
            bag[ch] -= 1
            count -= 1
            if bag[ch] < 0:
                count += 1
            if count == 0:
                return i - wnd + 1, True
        else:
            count = wnd
    return False, count


if __name__ == "__main__":
    print(solution(text, st))
