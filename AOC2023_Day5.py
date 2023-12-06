""" ADVENT OF CODE 2023 """
import pathlib

def from_source_to_destination(seed_maps: list, source: int) -> int:
    """
    Calculates the destination based on a list of seed maps and a source value.

    Parameters:
    - seed_maps: List of seed maps, each represented as a tuple (delta, start, length).
    - source: The source value.

    Returns:
    - int: The calculated destination value.
    """
    for seed_map in seed_maps:
        if seed_map[1] <= source < seed_map[1] + seed_map[2]:
            delta = seed_map[0] - seed_map[1]
            return source + delta
    return source 

# Main function for Day 5, Part 1
def day5(file):
    """
    Solves Day 5, Part 1 of Advent of Code 2023.

    Parameters:
    - file: Input file containing seed information.
    """
    # Read input file
    input_file = pathlib.Path(file)
    seed_maps = dict()
    with input_file.open('r') as file:
        lines = file.readlines()

    # Collect seeds
    seeds = list(map(int, lines[0].strip().split(":")[1].split()))

    # Collect seed_maps
    map_lines = lines[2:]
    for line in map_lines:
        line_parts = line.strip().split()
        if not line_parts:
            seed_maps[key] = values
        elif not line_parts[0].isdigit():
            key = line_parts[0]
            values = []
        else:
            values.append(list(map(int, line_parts)))
    seed_maps[key] = values

    # Loop through seeds and apply translations
    locations = []
    for seed in seeds:
        for seed_map in seed_maps.values():
            seed = from_source_to_destination(seed_map, seed)
        locations.append(seed)
    # print solution
    print(min(locations))

day5("day5_input.txt")

# Part 2

def get_seeds(seeds: list) -> list:
    """
    Converts a flat list of seeds to a list of seed ranges.

    Parameters:
    - seeds: List of seed values.

    Returns:
    - list: List of seed ranges as tuples.
    """
    new_seeds = []
    cursor = 0
    while cursor+1 < len(seeds):
        # convert pairs into ranges
        seed_range = (seeds[cursor], seeds[cursor] + seeds[cursor+1])
        new_seeds.append(seed_range)
        cursor += 2
    return list(new_seeds)

def map_to_range(seed_map: list) -> tuple:
    """
    Extracts the range from a seed map.

    Parameters:
    - seed_map: Seed map represented as a list [delta, start, length].

    Returns:
    - tuple: Range as a tuple (start, end).
    """
    return (seed_map[1], seed_map[1] + seed_map[2])

def overlap(range1: tuple, range2: tuple) -> tuple:
    """
    Finds the overlap between two ranges.

    Parameters:
    - range1: First range as a tuple (start, end).
    - range2: Second range as a tuple (start, end).

    Returns:
    - tuple: Overlapping range as a tuple (start, end) or None if no overlap.
    """
    overlap_start = max(range1[0], range2[0])
    overlap_end = min(range1[1], range2[1])
    # return None if no overlap (start > end)
    if overlap_start >= overlap_end:
        return None
    return (overlap_start, overlap_end)

def minus(range1: tuple, range2: tuple) -> list:
    """
    Subtracts one range from another.

    Parameters:
    - range1: First range as a tuple (start, end).
    - range2: Second range as a tuple (start, end).

    Returns:
    - list: List of remaining ranges after subtraction.
    """
    # if equal return empty list
    if range1 == range2:
        return []
    # if range2 is subset of range1: possible 2 results (smaller and bigger values)
    elif overlap(range1, range2) == range2:
        retval = []
        if range1[0] != range2[0]:
            left_smaller = (range1[0], range2[0])
            retval.append(left_smaller)
        if range2[1] != range1[1]:
            left_bigger = (range2[1], range1[1])
            retval.append(left_bigger)
        return retval
    # overlap downside
    elif range1[0] < range2[1] < range1[1]:
        return [(range2[1], range1[1])]
    # overlap upperside
    elif range1[0] < range2[0] < range1[1]:
        return [(range1[0], range2[0])]
    # no overlap, return just range1
    else: 
        return [range1]

def range_in_map(seed_range: tuple, seed_map: list) -> tuple:
    """
    Checks if seed range has overlap with seed map.

    Parameters:
    - seed_range: Range as a tuple (start, end).
    - seed_map: Seed map represented as a list [delta, start, length].

    Returns:
    - tuple: Overlapping range as a tuple (start, end) or None if no overlap.
    """
    return overlap(seed_range, map_to_range(seed_map))

def from_source_to_destination_range(seed_maps: list, source_ranges: list) -> list:
    """
    Applies translations to a range of seeds using a list of seed maps.

    Parameters:
    - seed_maps: List of seed maps, each represented as a list [delta, start, length].
    - source_ranges: List of seed ranges as tuples.

    Returns:
    - list: List of destination ranges after applying translations.
    """
    destination_ranges = []
    # working list of source ranges
    while source_ranges:
        # take first of working list to apply translation
        source_range = source_ranges.pop(0)
        # keep track of matches, if not seed range just falls trough to next map (add whole range to destination ranges)
        no_matches = True
        # loop trough seed map translation ranges
        for seed_map in seed_maps:
            # check overlap with translation range
            in_map = range_in_map(source_range, seed_map)
            # if overlap, translate and add to destinations list
            if in_map:
                no_matches = False
                delta = seed_map[0] - seed_map[1]
                destination_ranges.append((in_map[0] + delta, in_map[1] + delta))
                # check whether there are ranges left to translate further
                leftover = minus(source_range, in_map)
                # if ranges left add to working list 
                if leftover:
                    source_ranges.extend(leftover)
                # stop this cycle (leftover added to working list)
                break
        # keep track of matches, if not seed range just falls trough to next map (add whole range to destination ranges)
        if no_matches:
            destination_ranges.append(source_range)            
    return destination_ranges

def day5_2(file):
    """
    Solves Day 5, Part 2 of Advent of Code 2023.

    Parameters:
    - file: Input file containing seed information.
    """
    # Read input file
    input_file = pathlib.Path(file)
    seed_maps = dict()
    with input_file.open('r') as file:
        lines = file.readlines()

    # Collect seeds
    seeds = get_seeds(list(map(int, lines[0].strip().split(":")[1].split())))

    # Collect seed_maps
    map_lines = lines[2:]
    for line in map_lines:
        line_parts = line.strip().split()
        if not line_parts:
            seed_maps[key] = values
        elif not line_parts[0].isdigit():
            key = line_parts[0]
            values = []
        else:
            values.append(list(map(int, line_parts)))
    seed_maps[key] = values

    # Loop through seeds and apply translations
    locations = []
    for seed in seeds:
        seed = [seed]
        for translate in seed_maps.values():
            seed = from_source_to_destination_range(translate, seed)
        locations.append(seed)
    # print solution
    print(min(sum(locations, []))[0])

day5_2("day5_input.txt")
