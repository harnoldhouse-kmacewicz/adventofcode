#!/usr/bin/python3

adapters_3_jolts = 1 #at the end add 3
adapters_1_jolts = 1 #start from 1

with open('./input.txt', 'r') as input:
    list_lines = input.read().split('\n')
    list_lines = [int(item) for item in list_lines]
    list_lines.sort()
    for i in range(len(list_lines)-1):
        if (list_lines[i+1] - list_lines[i] == 1):
            adapters_1_jolts += 1
        if (list_lines[i+1] - list_lines[i] == 3):
            adapters_3_jolts += 1
    print(adapters_3_jolts * adapters_1_jolts)

input.close()