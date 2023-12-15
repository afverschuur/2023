""" ADVENT OF CODE 2023 """

import pathlib

# Day 15

def get_hash(string: str) -> int:
    """
    Calculate a hash value for a given string.

    Args:
        string (str): The input string.

    Returns:
        int: The hash value.
    """
    value = 0
    for char in string:
        # Add the ASCII value of each character 
        value += ord(char)
        value *= 17
        value = value % 256
    return value

def day15(file):
    """
    Solve Day 15 problem.

    Args:
        file (str): The path to the input file.
    """
    # read input file
    input_file = pathlib.Path(file)
    with input_file.open('r') as file:
        data = file.readlines()
    steps = data[0].strip().split(',')
    total = 0
    # Calculate the hash for each step and accumulate the total
    for step in steps:
        total += get_hash(step)
    # solution
    print(total)

#day15("day15_input.txt")

# Part 2

def split_step(string: str) -> list:
    """
    Split a string into parts based on the sign and return a list.

    Args:
        string (str): The input string.

    Returns:
        list: A list containing the parts of the string.
    """
    # get operation sign and replace by '|' to use split() method
    if string.count('=') > 0:
        operation = '='
        string = string.replace('=', '|')
    elif string.count('-') > 0:
        operation = '-'
        string = string.replace('-', '|')
    else:
        raise Exception("no sign in step!")
    split = string.split('|')
    # add operation sign to return value
    split.insert(1, operation)
    return split

class Box:
    """
    Class representing a box with lenses.
    """
    def __init__(self, number: int) -> None:
        self.number = number
        self.lensholders = []

    class LensHolder:
        """
        Class representing a lens holder inside a box.
        """
        def __init__(self, label: str, focal_length: int) -> None:
            self.label = label
            self.focal_length = focal_length

    def add_lens(self, label: str, focal_length: int) -> None:
        """
        Add a lens to the box.

        Args:
            label (str): The label of the lens.
            focal_length (int): The focal length of the lens.
        """
        exists = False
        for lensholder in self.lensholders:
            # If the lens already exists, update its focal length
            if lensholder.label == label:
                lensholder.focal_length = focal_length
                exists = True
                break
        # If the lens doesn't exist, add it to the box
        if not exists:
            self.lensholders.append(Box.LensHolder(label, focal_length))

    def _find_lensholder(self, label: str) -> int:
        """
        Find the index of a lens holder in the box.

        Args:
            label (str): The label of the lens holder.

        Returns:
            int: The index of the lens holder.
        """
        for index, lensholder in enumerate(self.lensholders):
            if lensholder.label == label:
                return index
        return -1

    def remove_lens(self, label: str) -> None:
        """
        Remove a lens from the box.

        Args:
            label (str): The label of the lens.
        """
        index = self._find_lensholder(label)
        # If the lens exists, remove it from the box
        if index > -1:
            self.lensholders.pop(index)

    def get_focussing_power(self) -> int:
        """
        Calculate the focusing power of the box.

        Returns:
            int: The focusing power.
        """
        box_multiplier = self.number + 1
        totalpower = 0
        # Calculate the total focusing power based on the lens focal lengths and their positions
        for lensholder in self.lensholders:
            totalpower += box_multiplier * (self._find_lensholder(lensholder.label) + 1) * int(lensholder.focal_length)
        return totalpower
    
    def __str__(self) -> str:
        """
        Represent the box as a string.

        Returns:
            str: The string representation of the box.
        """
        string = f"Box {self.number}: "
        for lensholder in self.lensholders:
            string += f"[{lensholder.label} {lensholder.focal_length}]"
        return string

def day15_2(file):
    """
    Solve Part 2 of Day 15 problem.

    Args:
        file (str): The path to the input file.
    """
    # read input file
    input_file = pathlib.Path(file)
    with input_file.open('r') as file:
        data = file.readlines()
    steps = data[0].strip().split(',')
    boxes = dict()
    # follow the steps
    for step in steps:
        parts = split_step(step)
        label = parts[0]
        operation = parts[1]
        focal_length = parts[2]
        box = get_hash(label)

        # get box, if not exists add box
        if box in boxes.keys():
            current_box = boxes[box]
        else:
            current_box = Box(box)
            boxes[box] = current_box

        # If the operation is '=', add the lens to the box
        if operation == '=':
            current_box.add_lens(label, focal_length)
        # If the operation is '-', remove the lens from the box
        elif operation == '-':
            current_box.remove_lens(label)
        else:
            raise Exception("unknown operation")
    
     # Calculate the total focusing power of all boxes
    total = 0
    for box in boxes.keys():
        total += boxes[box].get_focussing_power()
    # solution
    print(total)
        
day15_2("day15_input.txt")
