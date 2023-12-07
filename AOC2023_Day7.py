""" ADVENT OF CODE 2023 """
import pathlib

def hand_pattern(hand: str, joker=False) -> list:
    """
    Generates a pattern based on the hand of cards.

    Parameters:
    - hand: A string representing the hand of cards.
    - joker: A boolean indicating whether Jokers should be considered.

    Returns:
    - list: A list representing the card pattern.
    """
    pattern = []
    counted = []    
    jokers = 0
    max_count = 0

    # Count the occurrence of each card for the pattern
    for c in hand:
        if joker and c == 'J':
            jokers = hand.count('J')
            continue
        if not c in counted: 
            pattern.append(hand.count(c))
            counted.append(c)

    # For part 2, add jokers to the max to get the highest combination
    if joker:
        if pattern:
            max_count = max(pattern)
            pattern.remove(max_count)
        new_max = max_count + jokers
        pattern.append(new_max)
    
    return pattern

def card_points(card: str, joker=False) -> int:
    """
    Assigns points to a card.

    Parameters:
    - card: A string representing the card.
    - joker: A boolean indicating whether Jokers should be considered.

    Returns:
    - int: The assigned points.
    """
    if card == 'A':
        return 14
    if card == 'K':
        return 13
    if card == 'Q':
        return 12
    if card == 'J':
        if joker:
            return 1
        return 11
    if card == 'T':
        return 10
    return int(card)

def hand_points_pattern(hand: str, joker=False) -> list:
    """
    Generates a list of points based on the hand of cards.

    Parameters:
    - hand: A string representing the hand of cards.
    - joker: A boolean indicating whether Jokers should be considered.

    Returns:
    - list: A list representing the points of each card in the hand.
    """
    return [card_points(c, joker) for c in hand]

def compare(hand1: str, hand2: str, joker=False) -> int:
    """
    Compares two hands of cards.

    Parameters:
    - hand1: A string representing the first hand of cards.
    - hand2: A string representing the second hand of cards.
    - joker: A boolean indicating whether Jokers should be considered.

    Returns:
    - int: 1 if hand1 is greater, -1 if hand2 is greater, 0 if they are equal.
    """
    hand_pattern1 = hand_pattern(hand1, joker)
    hand_pattern2 = hand_pattern(hand2, joker)

    # Five > Four > Three of a kind > Pairs
    if max(hand_pattern1) > max(hand_pattern2):
        return 1
    if max(hand_pattern2) > max(hand_pattern1):
        return -1

    # Full House > Three of a kind (list shorter)
    # Two pairs > One Pair (list shorter)
    if max(hand_pattern1) == max(hand_pattern2):
        if len(hand_pattern1) < len(hand_pattern2):
            return 1
        if len(hand_pattern2) < len(hand_pattern1):
            return -1

    # Leftover: High Card
    cursor = 0 
    hand_points1 = hand_points_pattern(hand1, joker)
    hand_points2 = hand_points_pattern(hand2, joker)

    # Second ordering: highest card starting from the head
    while cursor < len(hand_points1):
        if hand_points1[cursor] > hand_points2[cursor]:
            return 1
        if hand_points2[cursor] > hand_points1[cursor]: 
            return -1
        cursor += 1
    # Same 
    return 0

def insert_ranklist(rank_list, card_tuple, joker=False):
    """
    Inserts a card into a rank list.

    Parameters:
    - rank_list: The rank list to insert the card into.
    - card_tuple: A tuple representing the card and its bid.
    - joker: A boolean indicating whether Jokers should be considered.

    Returns:
    - list: The updated rank list.
    """
    # Start list with the first entry
    if len(rank_list) == 0:
        rank_list.append(card_tuple)
    else:
        cursor = 0
        
        # Find the right place to insert by comparing until not greater (no cards are equal)
        while compare(card_tuple[0], rank_list[cursor][0], joker) > 0:
            cursor += 1
            if cursor > len(rank_list) - 1:
                break

        rank_list.insert(cursor, card_tuple)
    
    return rank_list

# Day 7
def day7(file, joker=False):
    """
    Solves Day 7 of Advent of Code 2023.

    Parameters:
    - file: Input file containing the hand of cards and bids.
    - joker: A boolean indicating whether Jokers should be considered.
    """
    ranklist = []

    # Read input
    input_file = pathlib.Path(file)
    with input_file.open('r') as file:
        # Loop through input to build a sorted list
        for line in file:
            card = line.strip().split()[0]
            bid = int(line.strip().split()[1])
            # Keep card and bid together to rank
            card_tuple = (card, bid)
            # Add to ranklist
            ranklist = insert_ranklist(ranklist, card_tuple, joker)
    
    # Calculate winnings
    rank = 1
    winnings = 0
    for card_tuple in ranklist:
        winnings += rank * card_tuple[1]
        rank += 1

    # Print solution
    print(winnings)

day7("day7_input.txt")

# Part 2
day7("day7_input.txt", True)
