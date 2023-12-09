""" ADVENT OF CODE 2023 """

import pathlib

def read_input(file):
    """
    Read input from a file and parse it into a list of lists.

    Args:
        file (str): The path to the input file.

    Returns:
        list: A list of lists containing integers.
    """
    data = []
    input_file = pathlib.Path(file)
    with input_file.open('r') as file:
        for line in file:
            # Parse each line into a list of integers and append to data
            history = list(map(int, line.strip().split()))
            data.append(history)
    return data

def get_differences(lst: list) -> list:
    """
    Calculate the differences between consecutive elements in a list.

    Args:
        lst (list): The input list.

    Returns:
        list: A list containing the differences between consecutive elements.
    """
    diff_list = []
    cursor = 0
    while cursor + 1 < len(lst):
        # Calculate and append the difference between consecutive elements
        diff = lst[cursor + 1] - lst[cursor]
        diff_list.append(diff)
        cursor += 1
    return diff_list

def get_lasts(lst: list) -> list:
    """
    Extract the last element from each list in a list of lists.

    Args:
        lst (list): The input list of lists.

    Returns:
        list: A list containing the last element from each list.
    """
    lasts = []
    for e in lst:
        # Append the last element from each list to the lasts list
        lasts.append(e[-1])
    return lasts

def get_next(lst: list) -> int:
    """
    Calculate the next element in a sequence.

    Args:
        lst (list): The input sequence.

    Returns:
        int: The next element in the sequence.
    """
    cursor = 0
    next = lst[cursor]
    while cursor + 1 < len(lst):
        # Calculate the sum of elements in the list
        cursor += 1
        next += lst[cursor]
    return next

def is_all_null(lst:list) -> bool:
    """
    Check if all elements in a list are zero.

    Args:
        lst (list): The input list.

    Returns:
        bool: True if all elements are zero, False otherwise.
    """
    for e in lst:
        # Check if any element in the list is non-zero
        if e != 0:
            return False
    return True

def day9(file, part2=False):
    """
    Solve Day 9 problem.

    Args:
        file (str): The path to the input file.
        part2 (bool): Flag indicating whether to consider part 2.

    """
    data = read_input(file)
    predictions = []
    for history in data:
        sequences = []
        diff = history
        sequences.append(history)
        while True:
            # Generate sequences and append to the sequences list
            diff = get_differences(diff)
            sequences.append(diff)
            # Break the loop if all differences are zero
            if is_all_null(diff):
                break
        sequences.reverse()
        if part2:
            # Calculate and append the prediction using part 2 logic
            predictions.append(get_prev(get_firsts(sequences)))
        else:
            # Calculate and append the prediction using part 1 logic
            predictions.append(get_next(get_lasts(sequences)))
    print(sum(predictions))

# part 2

def get_firsts(lst: list) -> list:
    """
    Extract the first element from each list in a list of lists.

    Args:
        lst (list): The input list of lists.

    Returns:
        list: A list containing the first element from each list.
    """
    firsts = []
    for e in lst:
        # Append the first element from each list to the firsts list
        firsts.append(e[0])
    return firsts

def get_prev(lst: list) -> int:
    """
    Calculate the previous element in a sequence.

    Args:
        lst (list): The input sequence.

    Returns:
        int: The previous element in the sequence.
    """
    cursor = 1
    prev = lst[0]
    while cursor < len(lst):
        # Calculate the sum of elements in the list in reverse order
        prev = lst[cursor] - prev
        cursor += 1
    return prev

day9("day9_input.txt", True)
