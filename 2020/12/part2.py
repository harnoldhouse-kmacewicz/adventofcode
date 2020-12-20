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

def calculate_direction(rotate, waypoint_position):
    next_waypoint_position = {}
    parse_rotate = re.split("(R|L)", rotate)
    parse_rotate = list(filter(None, parse_rotate))
    if parse_rotate[0] == "L":
        calculated_direction = direction["N"] - int(parse_rotate[1])
        if calculated_direction < 0:
            calculated_direction = 360 + calculated_direction
        next_waypoint_position[direction_reverse[calculated_direction]] = waypoint_position["N"]
        calculated_direction = direction["E"] - int(parse_rotate[1])
        if calculated_direction < 0:
            calculated_direction = 360 + calculated_direction
        next_waypoint_position[direction_reverse[calculated_direction]] = waypoint_position["E"]
        calculated_direction = direction["S"] - int(parse_rotate[1])
        if calculated_direction < 0:
            calculated_direction = 360 + calculated_direction
        next_waypoint_position[direction_reverse[calculated_direction]] = waypoint_position["S"]
        calculated_direction = direction["W"] - int(parse_rotate[1])
        if calculated_direction < 0:
            calculated_direction = 360 + calculated_direction
        next_waypoint_position[direction_reverse[calculated_direction]] = waypoint_position["W"]
    if parse_rotate[0] == "R":
        calculated_direction = direction["N"] + int(parse_rotate[1])
        if calculated_direction > 270:
            calculated_direction = calculated_direction - 360
        next_waypoint_position[direction_reverse[calculated_direction]] = waypoint_position["N"]
        calculated_direction = direction["E"] + int(parse_rotate[1])
        if calculated_direction > 270:
            calculated_direction = calculated_direction - 360
        next_waypoint_position[direction_reverse[calculated_direction]] = waypoint_position["E"]
        calculated_direction = direction["S"] + int(parse_rotate[1])
        if calculated_direction > 270:
            calculated_direction = calculated_direction - 360
        next_waypoint_position[direction_reverse[calculated_direction]] = waypoint_position["S"]
        calculated_direction = direction["W"] + int(parse_rotate[1])
        if calculated_direction > 270:
            calculated_direction = calculated_direction - 360
        next_waypoint_position[direction_reverse[calculated_direction]] = waypoint_position["W"]

    return next_waypoint_position

count = 0

waypoint_position = {
    "N": 1,
    "E": 10,
    "S": 0,
    "W": 0
}

with open('./input.txt', 'r') as input:
    list_lines = input.read().split('\n')
    for line in list_lines:
        current_line_parsed = re.split("(R|L|N|S|E|W|F)", line)
        current_line_parsed = list(filter(None, current_line_parsed))
        if current_line_parsed[0] == "R" or current_line_parsed[0] == "L":
            waypoint_position = calculate_direction("".join(current_line_parsed),  waypoint_position)
        if current_line_parsed[0] == "N":
            waypoint_position["N"] = waypoint_position["N"] + int(current_line_parsed[1])
        if current_line_parsed[0] == "S":
            waypoint_position["S"] = waypoint_position["S"] + int(current_line_parsed[1])
        if current_line_parsed[0] == "E":
            waypoint_position["E"] = waypoint_position["E"] + int(current_line_parsed[1])
        if current_line_parsed[0] == "W":
            waypoint_position["W"] = waypoint_position["W"] + int(current_line_parsed[1])
        if current_line_parsed[0] == "F":
            result["N"] = result["N"] + waypoint_position["N"] * int(current_line_parsed[1])
            result["E"] = result["E"] + waypoint_position["E"] * int(current_line_parsed[1])
            result["S"] = result["S"] + waypoint_position["S"] * int(current_line_parsed[1])
            result["W"] = result["W"] + waypoint_position["W"] * int(current_line_parsed[1])

    print(abs(result["N"] - result["S"]) + abs(result["E"] - result["W"]))

input.close()