""" ADVENT OF CODE 2023 """
import pathlib
import math
import numpy 

# Day 6 

def calculate_distance(push: int, time: int) -> int:
    """
    Calculates the distance for a given push and time.

    Parameters:
    - push: The push value.
    - time: The time value.

    Returns:
    - int: The calculated distance.
    """
    return (time - push) * push

def calculate_options(time_distance: tuple) -> int:
    """
    Brute-force solution to calculate options based on time and distance.

    Parameters:
    - time_distance: Tuple containing time and distance.

    Returns:
    - int: The calculated number of options.
    """
    options = []
    time = time_distance[0]
    min_distance = time_distance[1]

    # For every push option, calculate distance and keep if distance is greater than min_distance
    for push in range(time):
        distance = calculate_distance(push, time)
        if distance > min_distance:
            options.append(push)
    return options

def calculate_D(a: float, b: float, c: float) -> float:
    """
    Calculates the discriminant for a quadratic equation.

    Parameters:
    - a, b, c: Coefficients of the quadratic equation.

    Returns:
    - float: The calculated discriminant.
    """
    return b ** 2 - 4 * a * c

def solve_with_abc(a: float, b: float, c: float) -> list:
    """
    Solves a quadratic equation using the abc-formula.

    Parameters:
    - a, b, c: Coefficients of the quadratic equation.

    Returns:
    - list: List of solutions.
    """
    discriminant = calculate_D(a, b, c)
    # no solutions
    if discriminant < 0:
        return []
    # 1 solution
    elif discriminant == 0:
        return [-(b / (2 * a))]
    # 2 solutions
    else:
        return sorted([(-b - math.sqrt(discriminant)) / (2 * a), (-b + math.sqrt(discriminant)) / (2 * a)])

def calculate_options_abc(time_distance: tuple) -> int:
    """
    Solution using the abc-formula to calculate options based on time and distance.

    Parameters:
    - time_distance: Tuple containing time and distance.

    Returns:
    - int: The calculated number of options.
    """
    # Quadratic equation: -push^2 + time * push - distance = 0
    # Coefficients: a = -1, b = time, c = -distance
    solutions = solve_with_abc(-1, time_distance[0], -time_distance[1])
    return math.ceil(solutions[1]) - (math.floor(solutions[0]) + 1)

def day6(file):
    """
    Solves Day 6, Part 1 of Advent of Code 2023.

    Parameters:
    - file: Input file containing time and distance information.
    """
    # Import data
    input_file = pathlib.Path(file)
    with input_file.open('r') as file:
        lines = file.readlines()

    # Combine data to a list of time distances as tuples
    time_distances = list(zip(map(int, lines[0].strip().split(":")[1].split()), map(int, lines[1].strip().split(":")[1].split())))
    
    # Loop through time distances to collect the number of options
    ways_to_win = []
    for time_distance in time_distances:
        options = calculate_options_abc(time_distance)
        ways_to_win.append(options)

    # Print the solution
    print(numpy.prod(ways_to_win))

day6("day6_input.txt")

# Part 2

def day6_2(file):
    """
    Solves Day 6, Part 2 of Advent of Code 2023.

    Parameters:
    - file: Input file containing time and distance information.
    """
    # Import data
    input_file = pathlib.Path(file)
    with input_file.open('r') as file:
        lines = file.readlines()

    # Combine data to one time distance tuple
    time_distance = int(lines[0].strip().split(":")[1].replace(" ", "")), int(lines[1].strip().split(":")[1].replace(" ", ""))

    # Calculate the options
    options = calculate_options_abc(time_distance)

    # Print the solution
    print(options)

day6_2("day6_input.txt")
