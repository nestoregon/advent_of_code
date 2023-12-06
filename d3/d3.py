from typing import Tuple

with open("input.txt") as f:
    lines = f.readlines()
    input = [line.strip() for line in lines]

    lines = []
    for line in input:
        list_chars = [char for char in line]
        lines.append(list_chars)

DIRECTIONS = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
    (1, 1),
    (-1, -1),
    (-1, 1),
    (1, -1),
]


def is_symbol_adjacent(lines, x, y):
    for direction in DIRECTIONS:
        dx, dy = direction
        nx, ny = x + dx, y + dy

        if 0 <= nx < len(lines[y]) and 0 <= ny < len(lines):  # in bounds
            new_char = lines[ny][nx]
            if not new_char.isdigit() and new_char != '.':  # special char found!
                return True  # jackpot

    return False  # No special char found


def get_asterisc_coordinates_if_found(lines, x, y) -> Tuple[int, int]:
    for direction in DIRECTIONS:
        dx, dy = direction
        nx, ny = x + dx, y + dy

        if 0 <= nx < len(lines[y]) and 0 <= ny < len(lines):  # in bounds
            if lines[ny][nx] == '*':  # special char found!
                return (ny, nx)  # jackpot

    return (-1, -1)


def run(lines):
    p1_sol = 0
    p2_counter = {}
    p2_sol = 0
    for y in range(len(lines)):

        # reset
        number = ''
        adjacent_symbol = False
        asterisc = (-1, -1)

        for x in range(len(lines[y])):

            point = lines[y][x]
            if point.isdigit():
                adjacent_symbol = max(is_symbol_adjacent(lines, x, y), adjacent_symbol)
                asterisc = max(get_asterisc_coordinates_if_found(lines, x, y), asterisc)
                number += point
                continue

            # update scores
            if len(number) > 0:
                number = int(number)
                if adjacent_symbol:
                    p1_sol += number
                if asterisc != (-1, -1):
                    if asterisc not in p2_counter: p2_counter[asterisc] = number  # only 1 found
                    else: p2_sol += (p2_counter[asterisc] * number)  # update score

            # reset
            number = ''
            adjacent_symbol = False
            asterisc = (-1, -1)

        # update scores
        if len(number) > 0:
            number = int(number)
            if adjacent_symbol:
                p1_sol += number
            if asterisc != (-1, -1):
                if asterisc not in p2_counter: p2_counter[asterisc] = number  # only 1 found
                else: p2_sol += (p2_counter[asterisc] * number)  # update score

    return p1_sol, p2_sol


print(run(lines))
