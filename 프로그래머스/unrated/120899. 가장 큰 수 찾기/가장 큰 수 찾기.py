def solution(array):
    answer = []
    answer.append(max(array))
    largest = max(array)
    answer.append(array.index(largest))
    return answer