def solution(my_string):
    r= ""
    for i in my_string:
        if i.islower():
            r += i.upper()
        else:
            r += i.lower()
    return r