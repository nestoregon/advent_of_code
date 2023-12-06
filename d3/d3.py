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


def is_asterisc_adjacent(lines, x, y):
    for direction in DIRECTIONS:
        dx, dy = direction
        nx, ny = x + dx, y + dy

        if 0 <= nx < len(lines[y]) and 0 <= ny < len(lines):  # in bounds
            if lines[ny][nx] == '*':  # special char found!
                return f'{ny}-{nx}'  # jackpot

    return ''


def run(lines):
    p1_sol = 0
    p2_counter = {}
    p2_sol = 0
    for y in range(len(lines)):

        # reset
        number = ''
        adjacent_symbol = False
        astherisc_location = ''

        for x in range(len(lines[y])):

            point = lines[y][x]
            if point.isdigit():
                adjacent_symbol = max(is_symbol_adjacent(lines, x, y), adjacent_symbol)
                astherisc_location = max(is_asterisc_adjacent(lines, x, y), astherisc_location)
                number += point
                continue

            # update scores
            if len(number) > 0:
                number = int(number)
                if adjacent_symbol:
                    p1_sol += number
                if len(astherisc_location) > 0:
                    if astherisc_location not in p2_counter:
                        p2_counter[astherisc_location] = number
                    else:  # update solution if there's already 1 value
                        p2_sol += (p2_counter[astherisc_location] * number)

            # reset
            number = ''
            adjacent_symbol = False
            astherisc_location = ''

        # update scores
        if len(number) > 0:
            if adjacent_symbol:
                p1_sol += int(number)
            if len(astherisc_location) > 0:
                if astherisc_location not in p2_counter:
                    p2_counter[astherisc_location] = int(number)
                else:  # update solution if there's already 1 value
                    p2_sol += (p2_counter[astherisc_location] * int(number))

    return p1_sol, p2_sol


print(run(lines))
