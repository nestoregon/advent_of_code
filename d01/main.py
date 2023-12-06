"""
Classic situation where p1 is easy,
- p2 has to be rethought. Difficult solution = difficult implementation

Always find SIMPLEST algorithm first, then implement!
"""

with open("input.txt") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

MAP_CHARS_TO_INT = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}


def get_p1(lines):
    total = 0
    for line in lines:
        numbers = [char for char in line if char.isdigit()]
        two_digit_number = numbers[0] + numbers[-1]
        total += int(two_digit_number)
    return total


def get_matching_keys(chars: str):
    matches = [key for key in MAP_CHARS_TO_INT.keys() if key in chars]
    return matches


def check_if_any_match_is_one_to_one(matches, chars, reverse=False):
    for match in matches:
        chars_to_match = chars[:len(match)]
        if reverse:
            chars_to_match = chars[::-1][:len(match)][::-1]

        if chars_to_match == match:
            sol = MAP_CHARS_TO_INT[chars_to_match]
            return sol

    return None


def find_first_number_in_line(line, max_distance, reverse):
    num = None
    for i in range(len(line)):
        chars = line[i:i + max_distance]  # trim
        if reverse:
            chars = line[::-1][i:i + max_distance][::-1]  # reverse string, trim, unreverse

        # either is a number
        dict_reverse = {
            False: 0,
            True: -1
        }[reverse]
        if chars[dict_reverse].isdigit():
            return chars[dict_reverse]

        # or is a string
        matches = get_matching_keys(chars)
        num = check_if_any_match_is_one_to_one(matches, chars, reverse)
        if str(num).isdigit():
            return num

    raise KeyError(f'No number found in {line}')


def get_p2(lines):
    max_distance = max([len(number) for number in MAP_CHARS_TO_INT.keys()])  # 5
    total_sum = 0

    for line in lines:
        total_number = ''
        for reverse in [False, True]:  # check both ways
            num = find_first_number_in_line(line, max_distance, reverse)
            total_number += str(num)
        total_sum += int(total_number)

    return total_sum


p1 = get_p1(lines)
print(f'Part 1: {p1}')

p2 = get_p2(lines)
print(f'Part 2: {p2}')
