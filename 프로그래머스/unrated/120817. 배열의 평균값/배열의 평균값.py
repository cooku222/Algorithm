def solution(numbers):
    result = 0
    for number in numbers:
        result += number
    answer = result / len(numbers)
    return answer