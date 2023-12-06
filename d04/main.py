from collections import defaultdict

with open("input.txt") as f:
    lines = f.readlines()
    input = [line.strip() for line in lines]


def get_score_card_number_and_matching_numbers(line):
    """Formatting input."""
    score_card_number, score_card_data = line.split(': ')
    score_card_number = int(score_card_number.split(' ')[-1])

    score_card_data = score_card_data.strip().replace('  ', ' ')
    winning_numbers, my_numbers = score_card_data.split(' | ')

    winning_numbers = {int(x.strip()) for x in winning_numbers.split(' ')}  # yapf: disable
    my_numbers = {int(x.strip()) for x in my_numbers.split(' ')}  # yapf: disable

    matching_numbers = winning_numbers.intersection(my_numbers)  # intersection sets

    return matching_numbers, score_card_number


score_p1 = 0
score_cards = defaultdict(lambda: 1)  # to keep track, default 1
for line in input:
    matching_numbers, score_card_number = get_score_card_number_and_matching_numbers(line)

    # update score p1
    if len(matching_numbers) > 0:
        score_p1 += 2**(len(matching_numbers) - 1)

    next_score_cards_won = list(
        range(score_card_number + 1, score_card_number + len(matching_numbers) + 1)
    )
    # update score cards
    if len(matching_numbers) == 0: score_cards[score_card_number] += 0
    for won_card in next_score_cards_won:
        # you win as many score cards as many current cards you have
        score_cards[won_card] += score_cards[score_card_number]

score_p2 = sum(score_cards.values())

print(score_p1)
print(score_p2)
