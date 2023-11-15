def solution(n):
    if n % 2 == 0:
        even_list = list(range(1, n, 2))
        even_list.sort()
        return even_list
    else:
        odd_list = list(range(1, n + 1, 2))
        odd_list.sort()
        return odd_list