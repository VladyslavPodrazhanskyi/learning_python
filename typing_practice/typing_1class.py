"""
https://realpython.com/python-type-checking/#example-a-deck-of-cards

Classes as Types
There is a correspondence between classes and types.
For example, all instances of the Card class together form the Card type.
To use classes as types you simply use the name of the class.


To start with type checking, you need to get a type checker.
The easiest way to start is with mypy (http://mypy-lang.org/);
Other options:
pytype (from Google),
Pyright/Pylance (from Microsoft, bundled with VS
Code),
and Pyre (from Facebook) for alternatives.
PyCharm also bundles a type checking tool out of the box. Refer to your editor/type-checker documentation for
installation instructions.

"""

# game.py
from __future__ import annotations
import random
import sys
from typing import List, Tuple, Optional, Any, Sequence, TypeVar


# Choosable = TypeVar('Choosable', str, Card)


class Card:
    SUITS: List[str] = "♠ ♡ ♢ ♣".split()
    RANKS: List[str] = "2 3 4 5 6 7 8 9 10 J Q K A".split()

    def __init__(self, suit: str, rank: str) -> None:
        self.suit = suit
        self.rank = rank

    def __repr__(self) -> str:
        return f'{self.suit}{self.rank}'


class Deck:
    def __init__(self, cards: List[Card]) -> None:
        self.cards = cards

    """
    Mypy is able to connect your use of Card in the annotation with the definition of the Card class.
    This doesn’t work as cleanly though when you need to refer to the class currently being defined. 
    For example, the Deck.create() class method returns an object with type Deck. 
    However, you can’t simply add -> Deck as the Deck class is not yet fully defined.   
    
    from __future__ import annotations
     
    """

    @classmethod
    def create(cls, shuffle: bool = False) -> Deck:  # "Deck" or from __future__ import annotations
        """Create a new deck of 52 cards"""
        cards = [Card(s, r) for r in Card.RANKS for s in Card.SUITS]
        if shuffle:
            random.shuffle(cards)
        return cls(cards)

    def deal(self, num_hands: int):
        """Deal the cards in the deck into a number of hands"""
        cls = self.__class__
        return tuple(cls(self.cards[i::num_hands]) for i in range(num_hands))


class Player:
    def __init__(self, name: str, hand: Deck) -> None:
        self.name = name
        self.hand = hand

    def play_card(self) -> Card:
        """Play a card from the player's hand"""
        card = random.choice(self.hand.cards)
        self.hand.cards.remove(card)
        print(f'{self.name}: {card!r:<3} ', end='')
        return card


class Game:
    def __init__(self, *names: str):
        # Regarding type annotations: even though names will be a tuple of strings,
        # you should only annotate the type of each name. In other words, you should use str and not Tuple[str]:
        # Similarly, if you have a function or method accepting ** kwargs,
        # then you should only annotate the type of each possible keyword argument.
        """Set up the deck and deal cards to 4 players"""
        deck = Deck.create(shuffle=True)
        self.names = (list(names) + 'P1 P2 P3 P4'.split())[:4]
        self.hands = {
            n: Player(n, h) for n, h in zip(self.names, deck.deal(num_hands=4))
        }

    def play(self):
        """Play a card game"""
        start_player = random.choice(self.names)
        turn_order = self.player_order(start=start_player)
        # Play cards from each player's hand until empty
        while self.hands[start_player].hand.cards:
            for name in turn_order:
                self.hands[name].play_card()
            print()

    def player_order(self, start) -> Sequence[str]:
        """Rotate player order so that start goes first"""
        if start is None:
            start = random.choice(self.names)
        start_idx = self.names.index(start)
        return self.names[start_idx:] + self.names[:start_idx]


if __name__ == "__main__":
    player_names = sys.argv[1:]
    game = Game(*player_names)
    game.play()
    print(sys.argv)
