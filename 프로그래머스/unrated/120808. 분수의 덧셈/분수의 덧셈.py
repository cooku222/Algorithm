import math
def solution(numer1, denom1, numer2, denom2):
    answer = []
    son = numer1 * denom2 + numer2 * denom1
    mother = denom1 * denom2
    gcd = math.gcd(son, mother)
    return [son//gcd, mother//gcd]
    return answer