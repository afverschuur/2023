""" ADVENT OF CODE 2023 """
import pathlib

def read_grid(file):
    """Reads a grid from a text file.

    Args:
        file (str): The name of the input file.

    Returns:
        list: A 2D grid read from the file.
    """
    input_path = pathlib.Path(file)
    grid = []

    # Open the file and read each line
    with input_path.open('r') as file:
        for line in file:
            row = []
            # Iterate through characters in the line and append them to the row
            for c in line.strip():
                row.append(c)
            grid.append(row)
    
    return grid

def add_pos(pos1: tuple, pos2: tuple) -> tuple:
    """Adds two positions element-wise.

    Args:
        pos1 (tuple): The first position.
        pos2 (tuple): The second position.

    Returns:
        tuple: The result of the addition.
    """
    return (pos1[0] + pos2[0], pos1[1] + pos2[1])

def get_adjacent(pos: tuple) -> list:
    """Gets a list of adjacent positions to a given position.

    Args:
        pos (tuple): The position for which to find adjacent positions.

    Returns:
        list: List of adjacent positions.
    """
    steps = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    return [add_pos(pos, step) for step in steps]

def get_adjacent_in_grid(pos, grid) -> list:
    """Gets a list of adjacent positions within the grid boundaries.

    Args:
        pos (tuple): The position for which to find adjacent positions.
        grid (list): The 2D grid.

    Returns:
        list: List of adjacent positions within the grid boundaries.
    """
    max_x = len(grid)
    max_y = len(grid[0])
    return [pos for pos in get_adjacent(pos) if 0 <= pos[0] < max_x and 0 <= pos[1] < max_y]

def get_char_from_grid(pos, grid) -> chr:
    """Gets the character at a given position in the grid.

    Args:
        pos (tuple): The position in the grid.
        grid (list): The 2D grid.

    Returns:
        chr: The character at the specified position, None if out of boundaries
    """
    x = pos[0]
    y = pos[1]
    max_x = len(grid)
    max_y = len(grid[0])
    
    # Check if the position is within the grid boundaries
    if x >= max_x or y >= max_y:
        return None
    
    return grid[x][y]

def char_is_symbol(char: chr) -> bool:
    """Checks if a character is a symbol.

    Args:
        char (chr): The character to check.

    Returns:
        bool: True if the character is a symbol, False otherwise.
    """
    if char.isdigit() or char == '.':
        return False
    return True

def is_adjacent_to_symbol(pos, grid) -> bool:
    """Checks if any adjacent position contains a symbol.

    Args:
        pos (tuple): The position to check for adjacency.
        grid (list): The 2D grid.

    Returns:
        bool: True if any adjacent position contains a symbol, False otherwise.
    """
    # loop trough adjacent positions to find symbol
    for position in get_adjacent_in_grid(pos, grid):
        char = get_char_from_grid(position, grid)
        if char_is_symbol(char):
            return True
    return False

def day3(file):
    """Calculate and print the sum of numbers found adjacent to symbols in the grid.

    Args:
        file (str): The name of the input file.
    """
    grid = read_grid(file)
    max_x = len(grid)
    max_y = len(grid[0])
    x = 0
    y = 0
    number = ''
    found_adjacent = False
    part_numbers = []
    
    # Loop through each position in the grid
    while x < max_x:
        while y < max_y:
            char = get_char_from_grid((x, y), grid)
            
            # If the character is a digit, add it to the number
            if char.isdigit():
                number += char
                # If the position is adjacent to a symbol, set found_adjacent to True
                if is_adjacent_to_symbol((x, y), grid):
                    found_adjacent = True
            # If number is not empty, check if it's adjacent to a symbol and add to part_numbers
            elif number:
                if found_adjacent:
                    part_numbers.append(int(number))
                number = ''
                found_adjacent = False
            y += 1
        # If found_adjacent is True at the end of a row, add the number to part_numbers
        if found_adjacent:
            part_numbers.append(int(number))
        number = ''
        found_adjacent = False       
        y = 0
        x += 1
    # Print the sum of part_numbers
    print(sum(part_numbers))

day3("day3_input.txt")

# Part 2

def char_is_gear(char: chr) -> bool:
    """Checks if a character is a gear symbol.

    Args:
        char (chr): The character to check.

    Returns:
        bool: True if the character is a gear symbol, False otherwise.
    """
    return char == '*'

def get_whole_number(pos, grid) -> int:
    """Gets the whole number associated with a position in the grid.

    Args:
        pos (tuple): The position in the grid.
        grid (list): The 2D grid.

    Returns:
        int: The whole number, or -1 if not found.
    """
    if not get_char_from_grid(pos, grid).isdigit():
        return -1
    x = pos[0]
    y = pos[1] - 1
    char = get_char_from_grid((x, y), grid)
    
    # Find the first digit of the number the digit on pos is part of
    while char.isdigit():
        y -= 1
        char = get_char_from_grid((x, y), grid)
    
    first_digit_y = y + 1
    number = ''
    char = get_char_from_grid((x, first_digit_y), grid)
    y = first_digit_y
    
    # Get the whole number starting from the first digit
    while char and char.isdigit():
        number += char
        y += 1
        char = get_char_from_grid((x, y), grid)
    
    return int(number)

def get_adjacent_whole_numbers(pos, grid) -> list:
    """Gets a list of adjacent whole numbers to a position in the grid.

    Args:
        pos (tuple): The position for which to find adjacent whole numbers.
        grid (list): The 2D grid.

    Returns:
        list: List of adjacent whole numbers.
    """
    # use set to get unique numbers
    whole_numbers = set()
    adjacents = get_adjacent_in_grid(pos, grid)
    # loop trough adjecent positions to find whole numbers
    for adjacent in adjacents:
        number = get_whole_number(adjacent, grid)
        # if number found, add it to whole_numbers
        if number > 0:
            whole_numbers.update([number])
    return list(whole_numbers)

def day3_2(file):
    """Calculate and print the sum of gear ratios in the grid.

    Args:
        file (str): The name of the input file.
    """
    grid = read_grid(file)
    max_x = len(grid)
    max_y = len(grid[0])
    x = 0
    y = 0
    gear_ratios = []
    
    # Loop through each position in the grid
    while x < max_x:
        while y < max_y:
            char = get_char_from_grid((x, y), grid)
            
            # If the character is a gear symbol, get adjacent whole numbers and calculate gear ratio
            if char_is_gear(char):
                whole_numbers = get_adjacent_whole_numbers((x, y), grid)
                if len(whole_numbers) > 1:
                    gear_ratio = whole_numbers[0] * whole_numbers[1]
                    gear_ratios.append(gear_ratio)
            y += 1
        y = 0
        x += 1
    # Print the sum of gear_ratios
    print(sum(gear_ratios))

day3_2("day3_input.txt")
