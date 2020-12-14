#!/usr/bin/python3

input_list = []

current_point = 0
change_point = 0
accumulator = 0

with open('./input.txt', 'r') as input:
    list_lines = input.read().split('\n')
    for line in list_lines:
        temp_line = line.split()
        temp_line[1] = int(temp_line[1])
        temp_line.append(False)
        input_list.append(temp_line)
input.close()

while True:
    if input_list[current_point][2] == False:
        if input_list[current_point][0] == "acc":
            input_list[current_point][2] = True
            accumulator += input_list[current_point][1]
            current_point += 1
        elif input_list[current_point][0] == "nop":
            input_list[current_point][2] = True
            current_point += 1
        elif input_list[current_point][0] == "jmp":
            input_list[current_point][2] = True
            current_point += input_list[current_point][1]
    else:
        print(accumulator)
        break