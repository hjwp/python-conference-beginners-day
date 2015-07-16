# coding=utf8

"""
Challenge:  the Pythonic card deck class

Find out how to use magic methods so that the
following three standard functions work:

    import random
    deck = CardDeck()
    len(deck)
    print(deck[0])
    print(deck[-1])
    random.choice(deck)
    random.shuffle(deck)


Credit to Luciano Ramalho and his excellent book Fluent Python, from which
I stole this example.
"""



class CardDeck:

    ranks = [str(n) for n in range(2, 11)] + ['J', 'Q', 'K', 'A']
    suits = '♠♡♢♣'

    def __init__(self):
        self._cards = [
            rank + suit
            for suit in self.suits
            for rank in self.ranks
        ]

