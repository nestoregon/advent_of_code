import re
from typing import List

with open("input.txt") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]


def are_plays_valid(cubes) -> bool:
    cubes_available = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }
    for cube in cubes:  # play = "1 red, 2 green; 3 blue"
        num, color = cube.split(" ")
        if cubes_available[color] < int(num):
            return False
    return True


def get_minmum_cubes_needed_to_play(cubes: List[str]) -> int:
    min = {}
    for cube in cubes:  # play = "1 red, 2 green; 3 blue"
        num, color = cube.split(" ")
        num = int(num)
        if color not in min.keys():
            min[color] = num
        elif num > min[color]:
            min[color] = num

    # mult all values for score
    score = 1
    for color in min.values():
        score *= color
    return score


def run(lines):
    p1_score = 0
    p2_score = 0

    for line in lines:
        game, plays = line.split(": ")[:2]  # split game and plays
        _, num_game = game.split(" ")
        cubes = re.split("; |, ", plays)

        if are_plays_valid(cubes):  # is game valid?
            p1_score += int(num_game)

        p2_score += get_minmum_cubes_needed_to_play(cubes)

    print(p1_score)
    print(p2_score)


run(lines)
