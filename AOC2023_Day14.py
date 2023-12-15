""" ADVENT OF CODE 2023 """

import pathlib
import sys

# Day 14

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
            for char in line.strip():
                row.append(char)
            if line.strip():
                grid.append(row)
    return grid

def get_column(grid: list, index: int) -> list:
    """
    Get a column from the grid based on the given index.

    Args:
        grid (list): The input grid.
        index (int): The index of the column.

    Returns:
        list: The column from the grid.
    """
    col = []
    for row in grid:
        col.append(row[index])
    return col

def get_indices_of(char: chr, column: list) -> set:
    """
    Get the indices of a character in a column.

    Args:
        char (chr): The character to find.
        column (list): The column to search.

    Returns:
        set: A set containing the indices of the character in the column.
    """
    indices = []
    for index, spring in enumerate(column):
        if spring == char:
            indices.append(index)
    return indices

def roll_north(round_rocks: list, cube_rocks: list) -> list:
    """
    Simulate the rolling of rocks to the north.

    Args:
        round_rocks (list): The indices of round rocks in the column.
        cube_rocks (list): The indices of cube rocks in the column.

    Returns:
        list: The new positions of round rocks after rolling to the north.
    """
    round_rocks_north = []
    # because minimal added = 1 and first index must be 0 
    index = -1 
    # preserve original list when popping
    copy_round_rocks = round_rocks.copy() 
    copy_cube_rocks = cube_rocks.copy() 
    # start without obstacle
    obstacle = 0
    # locate first obstacle, if none set to maxvalue so that index round rock is always smaller
    next_obstacle = copy_cube_rocks.pop(0) if copy_cube_rocks else sys.maxsize
    # move trough list of round rocks
    while len(copy_round_rocks) > 0:
        round_rock = copy_round_rocks.pop(0)
        # if round rock is behind the current obstacle, check next obstacle
        if round_rock > obstacle:
            # if before next obstacle, roll to current obstacle
            if round_rock < next_obstacle:
                index += 1
            # if round rock behind next obstacle, check if it is behind more obstacles
            else:
                # if rock behind more obstacles find last obstacle it is behind and make that obstacle current obstacle
                while round_rock > next_obstacle:
                    obstacle = next_obstacle
                    next_obstacle = copy_cube_rocks.pop(0) if copy_cube_rocks else sys.maxsize
                # let it roll back to current obstacle
                index = obstacle+1
        # if round rock is before the current obstacle, roll to beginning
        else:
            index += 1
        # save new location
        round_rocks_north.append(index)
    return round_rocks_north

def print_grid(grid) -> None:
    """
    Print the grid.

    Args:
        grid (list): The grid to print.
    """
    print('\n')
    for row in grid:
        print_row = ''
        for char in row:
            print_row += char
        print(print_row)

def apply_gravity(grid: list) -> list:
    """
    Apply gravity to the grid.

    Args:
        grid (list): The input grid.

    Returns:
        list: The updated grid after applying gravity.
    """
    size = len(grid)
    # start new grid to return
    new_grid = [ [] for _ in range(size) ]
    # calculate new state for every column and build new grid (to visualize and use for further calculation)
    for col in range(len(grid[0])):
        column = get_column(grid, col)
        round_rocks = get_indices_of('O', column)
        cube_rocks = get_indices_of('#', column)
        # calculate new state
        new_state = roll_north(round_rocks, cube_rocks)
        # build new grid
        for index, row in enumerate(new_grid):
            if index in new_state:
                char = 'O'
            elif index in cube_rocks:
                char = '#'
            else:
                char = '.'
            row.append(char)
    return new_grid

def get_score(grid: list) -> int:
    """
    Calculate the score of the grid.

    Args:
        grid (list): The input grid.

    Returns:
        int: The score of the grid.
    """
    size = len(grid)
    totalscore = 0
    for index, row in enumerate(grid):
        totalscore += row.count('O') * (size - index)
    return totalscore

def day14(file):
    """
    Solve Day 14 problem.

    Args:
        file (str): The path to the input file.
    """
    # read input
    grid = read_grid(file)
    # apply gravity!
    grid = apply_gravity(grid)
    # solution
    print(get_score(grid))

# Part 2

def rotate_grid(grid: list) -> list:
    """
    Rotate the grid clockwise.

    Args:
        grid (list): The input grid.

    Returns:
        list: The rotated grid.
    """
    new_grid = []
    # rotate clockwise
    for index in range(len(grid[0])):
        new_row = []
        for row in grid:
            new_row.insert(0, row[index])
        new_grid.append(new_row)
    return new_grid

def perform_cycle(grid) -> list:
    """
    Perform one cycle of gravity simulation (north, then west, then south, then east).

    Args:
        grid (list): The input grid.

    Returns:
        list: The grid after one cycle of gravity simulation.
    """
    for _ in range(4):
        grid = apply_gravity(grid)
        grid = rotate_grid(grid)
    return grid

def day14_2(file):
    """
    Solve Part 2 of Day 14 problem.

    Args:
        file (str): The path to the input file.
    """
    # read input
    grid = read_grid(file)
    start_grid = grid.copy()
    history = []
    count = 0
    count_started = False
    # find start en size of cycle to reduce number of needed cycles to get to end state
    while True:
        grid = perform_cycle(grid)
        count += 1
        # check if curent state of grid happend before to find cycle 
        if grid in history:
            # if found start counting, if not already started
            if not count_started:
                start_cycle = count
                # clear history to find same state again
                history = []
                count_started = True
            # stop counting if started counting and stop performing cycles
            else:
                end_cycle = count
                count_started = False
                break 
        # build history
        history.append(grid)
    # calculate size of cycle
    cyclus = end_cycle - start_cycle
    # calculate equivalent steps using cycle and modulo calculation
    equal_cycles = (1000000000-start_cycle)%cyclus + start_cycle
    # perform equivalent steps to get end state
    for _ in range(equal_cycles):
        start_grid = perform_cycle(start_grid)
    # solution
    print(get_score(start_grid))

day14("day14_input.txt")
