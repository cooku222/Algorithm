def solution(my_string):
    answer = []
    for element in my_string:
        if element.isdecimal() == True:
            answer.append(int(element))
            answer.sort()
    return answer
    