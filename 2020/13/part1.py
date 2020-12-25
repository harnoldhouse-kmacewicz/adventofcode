#!/usr/bin/python3

with open('./input.txt', 'r') as input:
    list_lines = input.read().split('\n')
    timestamp = int(list_lines[0])
    buses = list_lines[1].replace("x,", "").split(",")
    resp_dict = {}
    for bus in buses:
        count_bus = int(bus)
        while True:
            if timestamp < count_bus:
                resp_dict[count_bus - timestamp] = (dict(bus = int(bus), timestamp = count_bus))
                break
            count_bus += int(bus)
    
    print(min(sorted(resp_dict)) * resp_dict[min(sorted(resp_dict))]["bus"])

input.close()