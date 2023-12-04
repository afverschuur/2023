""" ADVENT OF CODE 2023 """
import pathlib

# Day 4

def calculate_points(len_matches: int) -> int:
    """Calculate points based on the length of matching numbers.

    Args:
        len_matches (int): The length of matching numbers.

    Returns:
        int: The calculated points.
    """
    if not len_matches:
        return 0
    power = len_matches - 1
    return 2 ** power

def day4(file):
    """Calculate and print the total points for the lottery game.

    Args:
        file (str): The name of the input file.
    """
    total_points = 0
    input_file = pathlib.Path(file)

    # Open the file and read each line
    with input_file.open('r') as file:
        for line in file:
            # Split the line into parts
            parts = line.strip().split(":")
            numbers = parts[1]
            
            # Split the numbers into winning and lottery numbers
            split_numbers = numbers.split("|")
            winning_numbers = split_numbers[0].split()
            lottery_numbers = split_numbers[1].split()
            
            # Find the matches between winning and lottery numbers
            matches = [num for num in lottery_numbers if num in winning_numbers]
            
            # Calculate points based on the number of matches and update total_points
            points = calculate_points(len(matches))
            total_points += points
    
    print(total_points)

# day4("day4_input.txt")

# Part 2

def add_copy_of_cards(card: int, copies_of_cards: dict):
    """Add a copy of a card to the copies_of_cards dictionary.

    Args:
        card (int): The card number.
        copies_of_cards (dict): Dictionary to store the number of copies for each card.
    """
    if card not in copies_of_cards.keys():
        copies_of_cards[card] = 1
    else: 
        copies_of_cards[card] += 1 

def day4_2(file):
    """Calculate and print the total number of copies of cards for the lottery game.

    Args:
        file (str): The name of the input file.
    """
    copies_of_cards = dict()
    input_file = pathlib.Path(file)
    # current card to score
    card = 1

    # Open the file and read each line
    with input_file.open('r') as file:
        for line in file:
            # Add a copy of the current card to the dictionary
            add_copy_of_cards(card, copies_of_cards)
            
            # Loop through the copies of the current card
            for _ in range(copies_of_cards[card]):
                # Split the line into parts
                parts = line.strip().split(":")
                numbers = parts[1]
                
                # Split the numbers into winning and lottery numbers
                split_numbers = numbers.split("|")
                winning_numbers = split_numbers[0].split()
                lottery_numbers = split_numbers[1].split()
                
                # Find the matches between winning and lottery numbers
                matches = [num for num in lottery_numbers if num in winning_numbers]
                
                # add a copy for each match to following cards
                add_card = card
                for _ in matches:
                    add_card += 1
                    add_copy_of_cards(add_card, copies_of_cards)
            
            # Move to the next card
            card += 1
    
    # Print the sum of values in copies_of_cards
    print(sum(copies_of_cards.values()))

# solution 
day4_2("day4_input.txt")
