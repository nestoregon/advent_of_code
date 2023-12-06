from collections import defaultdict

with open("input.txt") as f:
    lines = f.readlines()
    input = [line.strip() for line in lines]

score_p1 = 0
score_cards = defaultdict(lambda: 1)  # to keep track, default 1
for line in input:
    card_seeing, score_card_data = line.split(': ')
    card_seeing = int(card_seeing.split(' ')[-1])

    score_card_data = score_card_data.strip().replace('  ', ' ')
    winning_numbers, my_numbers = score_card_data.split(' | ')

    winning_numbers = {int(x.strip()) for x in winning_numbers.split(' ')}  # yapf: disable
    my_numbers = {int(x.strip()) for x in my_numbers.split(' ')}  # yapf: disable

    # did i win?
    matching = winning_numbers.intersection(my_numbers)

    # update score p1
    if len(matching) > 0:
        score_p1 += 2**(len(matching) - 1)

    # update score p2
    next_score_cards_won = list(range(card_seeing + 1, card_seeing + len(matching) + 1))

    if len(matching) == 0: score_cards[card_seeing] += 0
    for card in next_score_cards_won:
        score_cards[card] += score_cards[card_seeing]

score_p2 = sum(score_cards.values())

print(score_p1)
print(score_p2)
