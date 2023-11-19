def solution(box, n):
    if (box[0] * box[1] * box[2]) % (n ** 3) == 0:
        return (box[0] * box[1] * box[2]) // (n ** 3)
    else:
        box.sort(reverse=False)
        return (box[0] // n) * (box[1] // n) * (box[2] // n)