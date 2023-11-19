def solution(num, k):
    x = [int(a) for a in str(num)]
    for element in x:
        if x.count(k) > 0:
            return x.index(k) + 1
        else:
            return -1