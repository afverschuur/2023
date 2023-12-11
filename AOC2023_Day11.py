""" ADVENT OF CODE 2023 """

import pathlib
from itertools import combinations

# Day 11

def read_grid(file):
    """ 
    Reads grid from a text file.

    Args:
        file (str): The path to the input file.

    Returns:
        list: A list representing the grid.
    """
    input_file = pathlib.Path(file)
    grid = []
    with input_file.open('r') as file:
        for line in file:
            row = []
            for c in line.strip():
                row.append(c)
            if line.strip():
                grid.append(row)
    return grid

def find_chars(char: chr, grid: list) -> tuple:
    """
    Find the coordinates of characters in the grid.

    Args:
        char (chr): The character to find.
        grid (list): The grid.

    Returns:
        tuple: A tuple containing the coordinates of characters.
    """
    x = 0
    chars = []
    for row in grid:
        y = 0
        for c in row:
            if c == char:
                chars.append((x, y))
            y += 1
        x += 1
    return chars

def find_empty_rows_columns(grid:list) -> tuple:
    """
    Find empty rows and columns in the grid.

    Args:
        grid (list): The grid.

    Returns:
        tuple: A tuple containing lists of empty rows and columns.
    """
    galaxies = find_chars('#', grid)
    # get rows and columns with galaxies
    xs = [tup[0] for tup in galaxies]
    ys = [tup[1] for tup in galaxies]
    # get dimensions
    grid_xs = range(len(grid))
    grid_ys = range(len(grid[0]))
    # check rows and columns for galaxies
    empty_rows = [x for x in grid_xs if x not in xs]
    empty_columns = [y for y in grid_ys if y not in ys]
    return (empty_rows, empty_columns)

def expand_universe(galaxies: list, empty_rows_columns: list, factor=2) -> list:
    """
    Expand the universe by a given factor!

    Args:
        galaxies (list): List of galaxy coordinates.
        empty_rows_columns (list): Lists of empty rows and columns.
        factor (int): Expansion factor.

    Returns:
        list: List of new galaxy coordinates after expansion.
    """
    new_galaxies = []
    for galaxy in galaxies:
        x = galaxy[0]
        y = galaxy[1]
        # check the number of rows/columns that expand with influence on the position of the galaxy
        expanding_rows = len([row for row in empty_rows_columns[0] if row < x])
        expanding_columns = len([col for col in empty_rows_columns[1] if col < y])
        # calculate coordinates of galaxy within the expanded universe
        x += expanding_rows * (factor - 1)
        y += expanding_columns * (factor - 1)
        new_galaxies.append((x, y))
    return new_galaxies

def calculate_distance(pair: tuple) -> int:
    """
    Calculate the Manhattan distance between two points.

    Args:
        pair (tuple): Tuple containing two points.

    Returns:
        int: The Manhattan distance.
    """
    pos1 = pair[0]
    pos2 = pair[1]
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def day11(file, factor=2):
    """
    Solve Day 11 problem.

    Args:
        file (str): The path to the input file.
        factor (int): Expansion factor for the universe.
    """
    grid = read_grid(file)
    empty_rows_columns = find_empty_rows_columns(grid)
    galaxies = find_chars('#', grid)
    # expand universe!
    galaxies = expand_universe(galaxies, empty_rows_columns, factor)
    # get all pairs of galaxies
    pairs = list(combinations(galaxies, 2))
    # calculate the total of the shortest paths
    total_distance = 0
    for pair in pairs:
        total_distance += calculate_distance(pair)
    print(total_distance)

day11("day11_input.txt", 1000000)
