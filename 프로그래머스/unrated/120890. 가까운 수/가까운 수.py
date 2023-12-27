import math
def solution(array, n):
    array.sort()
    diff = math.inf
    
    for num in array:
        _diff = abs(n - num)
        
        if _diff < diff:
            answer = num
            diff = _diff
            
    return answer