import random

card = ['Diamond', 'Club', 'Spade', 'Heart']

rank = [2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "Queen", "King", "Ace" ]



def random_Card():
    _card = random.choice(card)
    _rank = random.choice(rank)
    return (f"The {_rank} of {_card}")

print(random_Card())