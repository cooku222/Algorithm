def solution(n, numlist):
    answer = []
    for element in numlist:
        if element % n == 0:
            answer.append(element)
    return answer