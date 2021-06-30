import random

suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

deck = []
for suit in suits:
    for rank in ranks:
        deck.append(f'{rank} of {suit}')

print(f'There are {len(deck)} cards in the deck.')
print('Dealing ...')

hand = []
while len(hand) < 5:
    random.shuffle(deck)
    hand.append(deck.pop(0))

print(f'There are {len(deck)} cards in the deck.')
print(f'Player has the following cards in their hand:\n{hand}')