from collections import defaultdict

with open("input.txt") as f:
    lines = f.readlines()
    input = [line.strip() for line in lines]


def find_matching_numbers(score_card_data: str):
    score_card_data = score_card_data.strip().replace('  ', ' ')
    winning_numbers, my_numbers = score_card_data.split(' | ')
    winning_numbers = {int(x.strip()) for x in winning_numbers.split(' ')}  # yapf: disable
    my_numbers = {int(x.strip()) for x in my_numbers.split(' ')}  # yapf: disable

    # intersection of sets, find matching!
    matching_numbers = winning_numbers.intersection(my_numbers)
    return matching_numbers


score_p1 = 0
score_cards = defaultdict(lambda: 1)  # to keep track, default 1
for line in input:

    score_card_number, score_card_data = line.split(': ')
    score_card_number = int(score_card_number.split(' ')[-1])

    matching_numbers = find_matching_numbers(score_card_data)

    # update score p1
    if len(matching_numbers) > 0:
        score_p1 += 2**(len(matching_numbers) - 1)  # 2^0, 2^1, 2^2, ...

    next_score_cards_won = list(
        range(score_card_number + 1, score_card_number + len(matching_numbers) + 1)
    )  # if score card = 1, and len(matching_numbers) = 3, then you win 2, 3, 4

    # update score p2
    # you win as many score cards as many current cards you have
    for won_card in next_score_cards_won:
        score_cards[won_card] += score_cards[score_card_number]

    if len(matching_numbers) == 0: score_cards[score_card_number] += 0  # ensure current exists

score_p2 = sum(score_cards.values())

print(score_p1)
print(score_p2)
