from aoc2022.utils.get_lines import get_lines


lines = get_lines("i2.txt")

ENEMY_ROCK = "A"
ENEMY_PAPER = "B"
ENEMY_SCISSORS = "C"

PLAYER_SHOULD_LOSE = "X"
PLAYER_SHOULD_DRAW = "Y"
PLAYER_SHOULD_WIN = "Z"

RESULT_LOSE = 0
RESULT_DRAW = 3
RESULT_WIN = 6


picks_score = {
    "ROCK": 1,
    "PAPER": 2,
    "SCISSORS": 3,
}


def get_score_result(oponent, player):
    if oponent == ENEMY_ROCK:
        if player == PLAYER_SHOULD_DRAW:
            return RESULT_DRAW + picks_score["ROCK"]
        if player == PLAYER_SHOULD_LOSE:
            return RESULT_LOSE + picks_score["SCISSORS"]
        if player == PLAYER_SHOULD_WIN:
            return RESULT_WIN + picks_score["PAPER"]

    if oponent == ENEMY_PAPER:
        if player == PLAYER_SHOULD_DRAW:
            return RESULT_DRAW + picks_score["PAPER"]
        if player == PLAYER_SHOULD_LOSE:
            return RESULT_LOSE + picks_score["ROCK"]
        if player == PLAYER_SHOULD_WIN:
            return RESULT_WIN + picks_score["SCISSORS"]

    if oponent == ENEMY_SCISSORS:
        if player == PLAYER_SHOULD_DRAW:
            return RESULT_DRAW + picks_score["SCISSORS"]
        if player == PLAYER_SHOULD_LOSE:
            return RESULT_LOSE + picks_score["PAPER"]
        if player == PLAYER_SHOULD_WIN:
            return RESULT_WIN + picks_score["ROCK"]


total_score = 0

for line in lines:
    oponent = line[0]
    me = line[2]

    total_score += get_score_result(oponent, me)

print(total_score)
