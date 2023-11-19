def solution(numbers):
    if len(numbers) == 2:
        return (numbers[0]) * (numbers[1])
    else:
        numbers.sort(reverse=False)
        for i in numbers:
            if (numbers[0] * numbers[1]) > numbers[len(numbers) - 1] * numbers[len(numbers) - 2]:
                return (numbers[0] * numbers[1])
            else:
                return numbers[len(numbers) - 1] * numbers[len(numbers) - 2]
                
                
            