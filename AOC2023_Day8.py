""" ADVENT OF CODE 2023 """

import pathlib
from numpy import lcm  

def read_input(file) -> tuple:
    """
    Read input from a file and parse it into instructions and a network dictionary.

    Args:
        file (str): The path to the input file.

    Returns:
        tuple: A tuple containing instructions (str) and a network dictionary (dict).
    """
    # Read input from file
    input_file = pathlib.Path(file)
    with input_file.open('r') as file:
        data = file.readlines()
    
    instructions = data[0]
    nodes = data[2:]

    # Convert network nodes to a dictionary (parent:key, children:tuple)
    network = dict()
    for node in nodes:
        line = node.strip().split()
        network[line[0].strip()] = (line[2].strip('(,'), line[3].strip(')'))

    return (instructions, network)

def has_last_char_of(char: chr, string: str) -> bool:
    """
    Check if the last character of a string matches a specified character.

    Args:
        char (chr): The character to check for.
        string (str): The string to check.

    Returns:
        bool: True if the last character matches, False otherwise.
    """
    return string[-1] == char

def find_steps(loc: tuple, instructions: str, network: dict, part2=False) -> int:
    """
    Calculate the number of steps needed to reach a destination based on instructions.

    Args:
        loc (tuple): The current location (parent:key, children:tuple).
        instructions (str): A string of instructions.
        network (dict): The network dictionary.
        part2 (bool): Flag indicating whether to consider part 2.

    Returns:
        int: The number of steps needed.
    """
    cursor = 0
    steps = 0
    new_loc = loc[0]  # Initialize new_loc outside the loop

    while True:
        steps += 1
        instruction = instructions[cursor]
        
        if instruction == 'L':
            new_loc = loc[0]
        if instruction == 'R':
            new_loc = loc[1]
        
        if new_loc == 'ZZZ' or (part2 and has_last_char_of('Z', new_loc)):
            break

        loc = network[new_loc]
        cursor += 1
        # Start instructions again if necessary
        cursor = cursor % (len(instructions) - 1)

    return steps

def day8(file):
    """
    Solve Day 8 problem.

    Args:
        file (str): The path to the input file.
    """
    # Read input
    data = read_input(file)
    instructions = data[0]
    network = data[1]

    # Follow instructions to find steps
    steps = find_steps(network['AAA'], instructions, network)

    # Solution
    print(steps)

day8("day8_input.txt")

# Part 2

def day8_2(file):
    """
    Solve Part 2 of Day 8 problem.

    Args:
        file (str): The path to the input file.
    """
    # Read input
    data = read_input(file)
    instructions = data[0]
    network = data[1]

    # Find starting locations
    locations = [network[loc] for loc in network.keys() if has_last_char_of('A', loc)]

    # Follow instructions per location to find steps per location
    steps_locations = []
    for loc in locations:
        steps = find_steps(loc, instructions, network, part2=True)
        steps_locations.append(steps)

    # Solution is the least common multiple of all steps needed
    print(lcm.reduce(steps_locations))

day8_2("day8_input.txt")
