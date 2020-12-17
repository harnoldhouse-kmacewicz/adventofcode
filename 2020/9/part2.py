#!/usr/bin/python3

spawn_dict = {}
number_from_part_1 = 23278925

with open('./input.txt', 'r') as input:
    list_lines = input.read().split('\n')
    for i in range(len(list_lines)):
        spawn_dict[i] = int(list_lines[i])
input.close()

for item in spawn_dict:
    temp_list = []
    temp_list.append(spawn_dict[item])
    for iter_item in range(item+1, len(spawn_dict)):
        temp_list.append(spawn_dict[iter_item])
        if (sum(temp_list) == number_from_part_1):
            print(min(temp_list) + max(temp_list))
            break
        if (sum(temp_list) > number_from_part_1):
            break
