def solution(emergency):
    rank = [sorted(emergency, reverse=True).index(i)+1 for i in emergency] 
    return rank
    