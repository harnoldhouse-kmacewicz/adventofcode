#!/usr/bin/python3

index = 1
resp_dict = {}

with open('./input.txt', 'r') as input:
    line = input.read()

for init_value in line.split(","):
    resp_dict[index] = int(init_value)
    index = index+1

while index < 2021:
    list_to_iterate = list(resp_dict)[:-1]
    list_to_iterate.reverse()
    if any(resp_dict[key] == resp_dict[index-1] for key in list_to_iterate):
        for key_matched in list_to_iterate:
            if resp_dict[key_matched] == resp_dict[index-1]:
                resp_dict[index] = index -1 -key_matched
                break
    else:
        resp_dict[index] = 0

    index = index+1

print(resp_dict[2020])

input.close()