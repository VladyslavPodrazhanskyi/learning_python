"""
https://realpython.com/python-type-checking/#example-a-deck-of-cards
"""

# game.py

import random
from typing import List, Tuple, Optional, Any, Sequence, TypeVar

SUITS: List[str] = "♠ ♡ ♢ ♣".split()
RANKS: List[str] = "2 3 4 5 6 7 8 9 10 J Q K A".split()
Card = Tuple[str, str]
Deck = List[Card]
Choosable = TypeVar('Choosable', str, Card)


def create_deck(shuffle: bool = False) -> Deck:
    """Create a new deck of 52 cards"""
    deck = [(s, r) for r in RANKS for s in SUITS]
    if shuffle:
        random.shuffle(deck)
    return deck


def deal_hands(deck: Deck) -> Tuple[Deck, Deck, Deck, Deck]:
    """Deal the cards in the deck into four hands"""
    return deck[0::4], deck[1::4], deck[2::4], deck[3::4]


# Sequence can be thought of as a duck type,
# since it can be any object
# with .__len__() and .__getitem__()
# implemented.

def choose(items: Sequence[Choosable]) -> Choosable:
    """Choose and return a random item"""
    return random.choice(items)


#  --no-implicit-optional

def player_order(
    names: List[str],
    start: Optional[str] = None,
) -> Sequence[str]:
    if start is None:
        start = choose(names)
    start_idx = names.index(start)
    return names[start_idx:] + names[:start_idx]


def play() -> None:
    """Play a 4-player card game"""
    deck = create_deck(shuffle=True)
    names = "P1 P2 P3 P4".split()
    hands = {n: h for n, h in zip(names, deal_hands(deck))}
    # for name, cards in hands.items():
    #     card_str = " ".join(f"{s}{r}" for (s, r) in cards)
    #     print(f"{name}: {card_str}")
    start_player = choose(names)
    turn_order = player_order(names, start=start_player)
    while hands[start_player]:
        for name in turn_order:
            card = choose(hands[name])
            hands[name].remove(card)
            print(f'{name}: {card[0] + card[1]:<3}', end='')
        print()


if __name__ == "__main__":
    play()
