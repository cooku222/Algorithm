def solution(my_string, num1, num2):
    if my_string[num1] == my_string[num2]:
        return my_string
    else:
        my_string = my_string[0:(num1)] + my_string[num2] + my_string[(num1 + 1):(num2)] + my_string[num1] + my_string[(num2 + 1):(len(my_string))]
        return my_string