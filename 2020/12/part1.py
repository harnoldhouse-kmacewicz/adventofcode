#!/usr/bin/python3

import re, sys

result = {
    "N": 0,
    "S": 0,
    "E": 0,
    "W": 0
}

direction = {
    "N": 0,
    "E": 90,
    "S": 180,
    "W": 270
}

direction_reverse = {
    0: "N",
    90: "E",
    180: "S",
    270: "W"
}

def calculate_direction(current, rotate):
    parse_rotate = re.split("(R|L)", rotate)
    parse_rotate = list(filter(None, parse_rotate))
    if parse_rotate[0] == "L":
        rotated = direction[current] - int(parse_rotate[1])
        if rotated < 0:
            rotated = 360 + rotated
    if parse_rotate[0] == "R":
        rotated = direction[current] + int(parse_rotate[1])
        if rotated > 270:
            rotated = rotated - 360
            
    return direction_reverse[rotated]

count = 0
with open('./input.txt', 'r') as input:
    current_direction = "E"
    list_lines = input.read().split('\n')
    for line in list_lines:
        current_line_parsed = re.split("(R|L|N|S|E|W|F)", line)
        current_line_parsed = list(filter(None, current_line_parsed))
        if current_line_parsed[0] == "N":
            result["N"] += int(current_line_parsed[1])
        if current_line_parsed[0] == "S":
            result["S"] += int(current_line_parsed[1])
        if current_line_parsed[0] == "E":
            result["E"] += int(current_line_parsed[1])
        if current_line_parsed[0] == "W":
            result["W"] += int(current_line_parsed[1])
        if current_line_parsed[0] == "R" or current_line_parsed[0] == "L":
            current_direction = calculate_direction(current_direction, "".join(current_line_parsed))
        if current_line_parsed[0] == "F":
            result[current_direction] += int(current_line_parsed[1])
input.close()

print(abs(result["N"] - result["S"]) + abs(result["E"] - result["W"]))