from aoc2022.utils.get_lines import get_lines


lines = get_lines("i2.txt")

ENEMY_ROCK = "A"
ENEMY_PAPER = "B"
ENEMY_SCISSORS = "C"

PLAYER_ROCK = "X"
PLAYER_PAPER = "Y"
PLAYER_SCISSORS = "Z"

RESULT_LOSE = 0
RESULT_DRAW = 3
RESULT_WIN = 6

picks_score = {
    PLAYER_ROCK: 1,
    PLAYER_PAPER: 2,
    PLAYER_SCISSORS: 3,
}


def get_score_result(oponent, player):
    if oponent == ENEMY_ROCK:
        if player == PLAYER_PAPER:
            return RESULT_WIN
        if player == PLAYER_ROCK:
            return RESULT_DRAW
        if player == PLAYER_SCISSORS:
            return RESULT_LOSE

    if oponent == ENEMY_PAPER:
        if player == PLAYER_PAPER:
            return RESULT_DRAW
        if player == PLAYER_ROCK:
            return RESULT_LOSE
        if player == PLAYER_SCISSORS:
            return RESULT_WIN

    if oponent == ENEMY_SCISSORS:
        if player == PLAYER_PAPER:
            return RESULT_LOSE
        if player == PLAYER_ROCK:
            return RESULT_WIN
        if player == PLAYER_SCISSORS:
            return RESULT_DRAW


total_score = 0

for line in lines:
    oponent = line[0]
    me = line[2]

    total_score += picks_score[me]
    total_score += get_score_result(oponent, me)

print(total_score)
