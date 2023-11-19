def solution(order):
    answer = 0
    game = [int(a) for a in str(order)]
    for element in game:
        return game.count(3) + game.count(6) + game.count(9)
    