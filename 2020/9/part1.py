#!/usr/bin/python3

spawn_dict = {}
current_position = 25

with open('./input.txt', 'r') as input:
    list_lines = input.read().split('\n')
    for i in range(len(list_lines)):
        spawn_dict[i] = int(list_lines[i])
input.close()
        
for item in spawn_dict:
    passed = False
    for x in range(current_position-25, current_position):
        for y in range(current_position-25, current_position):
            if x != y:
                if (spawn_dict[x] + spawn_dict[y]) == spawn_dict[current_position]:
                    passed = True
    
    if passed == False:
        print(spawn_dict[current_position])
        break

    current_position += 1