
def most_frequent(numbers):
    '''
    Check what is the most frequent number in an array.

    >>> most_frequent([3, 3, 3, 2, 2, 2, 4, 4])
    3
    >>> most_frequent([3, 3, 2, 2, 2, 2, 4, 4])
    2
    '''
    
    number_values = {}
    for number in numbers:
        number_values[number] = number_values.get(number, 0) + 1
    most_frequent_number = [0,0]
    for key, value in number_values.items():
        if value > most_frequent_number[1]:
            most_frequent_number[0] = key
            most_frequent_number[1] = value
        elif value == most_frequent_number[1] and key > most_frequent_number[0]:
            most_frequent_number[0] = key
            most_frequent_number[1] = value
    return most_frequent_number[0]


def cyclic_rotation(letters, n):
    '''
    Move the last N elements from the end to the beginning.

    >>> cyclic_rotation('abcde', 3)
    'cdeab'
    >>> cyclic_rotation('abc', 1)
    'cab'
    '''

    letters = (letters[-n:] + letters[:-n]) 
    return letters


def poker_hand(cards):
    '''
    >>> poker_hand([1, 1, 1, 1, 1])
    'five'
    >>> poker_hand([2, 2, 2, 2, 3])
    'four'
    >>> poker_hand([1, 1, 1, 2, 3])
    'three'
    >>> poker_hand([2, 2, 3, 3, 4])
    'twopairs'
    >>> poker_hand([1, 2, 2, 3, 4])
    'pair'
    >>> poker_hand([1, 1, 2, 2, 2])
    'fullhouse'
    >>> poker_hand([1, 2, 3, 4, 6])
    'nothing'
    '''
    
    counted_cards = {}
    for card in cards:
        counted_cards[card] = counted_cards.get(card, 0) + 1   
    if 5 in counted_cards.values():
        return 'five'
    elif 4 in counted_cards.values():
        return 'four'
    elif 3 in counted_cards.values() and 2 not in counted_cards.values():
        return 'three'
    elif 2 in counted_cards.values() and 3 not in counted_cards.values():
        pair = 0
        for value in counted_cards.values():
            if value == 2:
                pair += 1
        if pair == 2:
            return 'twopairs'
        else:
            return 'pair'
    elif 3 in counted_cards.values() and 2 in counted_cards.values():
        return 'fullhouse'
    else:
        return 'nothing'