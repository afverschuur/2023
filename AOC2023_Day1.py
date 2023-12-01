""" ADVENT OF CODE 2023 """
import pathlib

# Day 1
def day1(file, part2=False) -> None:
    """
    Calculate the sum of numbers in a file. Optionally replace words with numbers based on a translation dictionary.

    Parameters:
    - file (str): The name of the input file.
    - part2 (bool): If True, replace words with numbers before calculating the sum.

    Returns:
    None (prints the sum of numbers)
    """
    # Create a Path object for the input file
    input_file = pathlib.Path(file)
    # List to store numbers from the file
    numbers = []
    
    # Open the input file for reading
    with input_file.open('r') as file:
        # Iterate through each line in the file
        for line in file:
            # If part2 is True, replace words with numbers in the line
            if part2:
                line = replace_number(line)
            
            # Extract and process individual digits from the line
            number = ''
            for c in line.strip():
                if c.isdigit():
                    # Handle multiple numbers (keep only first and last)
                    if len(number) > 1:
                        number = number[0] + c
                    else:
                        number += c
            
            # If only one digit is found, duplicate it to create a two-digit number
            if len(number) == 1:
                number *= 2
            # Convert the processed number to an integer and add it to the list
            numbers.append(int(number))
    
    # Print the sum of numbers
    print(sum(numbers))

#day1("day1_input.txt")

# Translation dictionary for word-to-number conversion (extra chars because possible overlap: threeight)
translate = {
    'one': '1e',
    'two': '2o',
    'three': '3e',
    'four': '4',
    'five': '5e',
    'six': '6',
    'seven': '7n', 
    'eight': '8t',
    'nine': '9e',
}

def find_number(string: str) -> bool:
    """
    Check if a given string contains any of the words from the translation dictionary.

    Parameters:
    - string (str): The input string to check.

    Returns:
    bool: True if any word is found, False otherwise.
    """
    global translate
    for word in translate.keys():
        # Check if the word is present in the string
        if string.find(word) > -1:
            return True
    return False

def replace_number(string: str) -> str:
    """
    Replace words in a string with their corresponding numbers based on the translation dictionary.

    Parameters:
    - string (str): The input string to perform replacements on.

    Returns:
    str: The modified string after word-to-number replacements.
    """
    global translate
    part = ''
    for c in string:
        part += c
        # If a word is found, replace it with its corresponding number
        if find_number(part):
            for word, number in translate.items():
                part = part.replace(word, number)
    return part

# Part 2
day1("day1_input.txt", True)