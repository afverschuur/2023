""" ADVENT OF CODE 2023 """
import pathlib

#Day 1
def day1(file, part2=False):
    input_file = pathlib.Path(file)
    numbers = []
    with input_file.open('r') as file:
        for line in file:
            if part2:
                line = replace_number(line)
            number = ''
            for c in line.strip():
                if c.isdigit():
                    if len(number) > 1:
                        number = number[0] + c
                    else:
                        number += c
            if len(number) == 1:
                number *= 2
            numbers.append(int(number))
    print(sum(numbers))

#Part 1
#day1("day1_input.txt")

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


def find_number(string:str) -> bool:
    global translate
    for word in translate.keys():
        if string.find(word) > -1:
            return True
    return False

def replace_number(string:str) -> str:
    global translate
    part = ''
    for c in string:
        part += c
        if find_number(part):
            for word, number in translate.items():
                part = part.replace(word, number)
    return part

# Part 2
day1("day1_input.txt", True)


















            
    

