""" ADVENT OF CODE 2023 """
import pathlib
import re

# Day 2

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

def day2(file) -> None:
    """
    Calculate and print the sum of IDs for valid games based on color conditions.

    Parameters:
    - file (str): The name of the input file.

    Returns:
    None (prints the sum of IDs)
    """
    input_file = pathlib.Path(file)
    possibilities = set()
    
    with input_file.open('r') as file:
        # Iterate through each line in the file
        for line in file:
            # Split the line into parts using ':'
            parts = line.split(sep=':')
            # Extract the game ID from the first part
            game = parts[0].split()
            id = int(game[1])
            # Extract and process individual game sets from the second part
            game_sets = parts[1].strip().split(sep=';')
            ok = True
            # Check color conditions for each color pair in each game set
            for game_set in game_sets:
                for color_pair in game_set.split(sep=','):
                    pair = color_pair.split()
                    # Check conditions for red color
                    if pair[1] == 'red' and int(pair[0]) > MAX_RED:
                        ok = False
                    # Check conditions for green color
                    if pair[1] == 'green' and int(pair[0]) > MAX_GREEN:
                        ok = False
                    # Check conditions for blue color
                    if pair[1] == 'blue' and int(pair[0]) > MAX_BLUE:
                        ok = False
            # If all conditions are met, add the ID to the set of possibilities
            if ok:
                possibilities.update([id])
    # Print the sum of IDs for valid games
    print(sum(list(possibilities)))

#day2("day2_input.txt")

def day2_2(file) -> None:
    """
    Calculate and print the product of maximum color values for each game set, and then print the sum of those products.

    Parameters:
    - file (str): The name of the input file.

    Returns:
    None (prints the list of products and their sum)
    """
    input_file = pathlib.Path(file)
    powers = []
    
    with input_file.open('r') as file:
        # Iterate through each line in the file
        for line in file:
            # Split the line into parts using ':'
            parts = line.split(sep=':')
            # Extract and process individual game sets from the second part
            game_sets = parts[1].strip().split(sep=';')
            max_red = 0
            max_green = 0
            max_blue = 0
            # Find the maximum values for red, green, and blue colors in each game set
            for game_set in game_sets:
                for color_pair in game_set.split(sep=','):
                    pair = color_pair.split()
                    # Update maximum value for red color
                    if pair[1] == 'red' and int(pair[0]) > max_red:
                        max_red = int(pair[0])
                    # Update maximum value for green color
                    if pair[1] == 'green' and int(pair[0]) > max_green:
                        max_green = int(pair[0])
                    # Update maximum value for blue color
                    if pair[1] == 'blue' and int(pair[0]) > max_blue:
                        max_blue = int(pair[0])
            # Calculate the product of maximum color values (power) and append it to the powers list
            power = max_blue * max_green * max_red
            powers.append(power)
    
    # Print the list of products and their sum
    print(list(powers))
    print(sum(list(powers)))

# Invoke the day2_2 function with the provided input file
day2_2("day2_input.txt")
