# -*- coding: utf-8 -*-

from enum import Enum, auto

__all__ = ['Card', 'Suit']

class Suit(Enum):
    Palace=auto()
    Library=auto()
    Garden=auto()
    Temple=auto()
    Stronghold=auto()
    NonSuit=auto()

__all_cards__ = []

class Card():
    # TODO is a Card really immutable?
    """
    Store every relevant attribute about the ToT cards.
    Create only one instance from each different card, and store it in __all_cards__
    list.
    """

    # for immutability use __slots__ instead of __dict__ to store attributes
    __slots__ = ['number', 'name', 'suit', 'initialized']
    def __new__(cls, *args, **kw):
        # TODO add description

        # If the class was called with positional argument then the number of the
        # card sould be the 0th element in the args list.
        # if the class was called without ani positional argument than the number
        # is stored in the kw dictionary
        if len(args):
            number = args[0]
        else:
            number = kw['number']
        # Check if this number was already defined
        card_idx = Card._find_id_in_card_list(number, __all_cards__)

        # if the card number havn't been already created create it and signal that
        # initialization still required for this class
        # else the already created and initialized instance is returned from the
        # __all_cards__ list
        if card_idx is None:
            instance = super().__new__(cls)
            __all_cards__.append(instance)
            card_idx = len(__all_cards__) - 1
            super(Card, instance).__setattr__('initialized', False)
            #instance.initialized = False

        return __all_cards__[card_idx]

    def __init__(self, number=0, name=None, suit=None):
        # TODO add description
        if self.initialized :
            # TODO add logging feautre here
            print("This item has been already initialized");
            return
        # because of the redefinition of __setattr__ the . notation doesn't work
        # use the super's setattr instead.
        #self.number=number
        #self.name=name
        #self.suit=suit
        #self.__initialized=True
        super().__setattr__('number', number)
        super().__setattr__('name', name)
        super().__setattr__('suit', suit)
        super().__setattr__('initialized', True)

    def __setattr__(self, name, value):
        """
        Remove the possibility to modify attributes, so the class becomes immutable
        """
        msg = "{} has no attribut {}".format(self.__class__, name)
        raise AttributeError(msg)

    def __str__(self):
        #s="number: {number}, name: {name}, suit: {suit}".format(**self.__dict__)
        s="number: {}, name: {}, suit: {}".format(self.number, self.name, self.suit)
        return s

    def __lt__(self, other):
        if isinstance(other, Card):
            return self.number < other.number
        else:
            return NotImplemented

    def __hash__(self):
        return hash(self.number)

    @classmethod
    def _find_id_in_card_list(cls, number, card_list):
        """
        Searches for the card number in the given card_list and returns it's index
        if found and None when not.
        """
        # TODO add proper description

        tmp_car = next(filter(lambda x: x[1].number == number, enumerate(card_list)), (None,None))
        return tmp_car[0]
