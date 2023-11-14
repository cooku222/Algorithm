import math
def solution(n):
    x = math.sqrt(n)
    if x == int(x):
        return 1
    else:
        return 2