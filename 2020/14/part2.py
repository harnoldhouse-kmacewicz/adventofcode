#!/usr/bin/python3

import re

resp_dict = {}

def dec_to_bin(x):
    return int(bin(x)[2:])

index_for_mem_cache = 0

with open('./input.txt', 'r') as input:
    list_lines = input.read().split("mask = ")
    list_lines = "++".join(list_lines)
    list_lines = list_lines.split("++")
    list_lines = list(filter(None, list_lines))
    for line in list_lines:
        for info in line.split("\n")[1:]:
            if info != "":
                mem_number = re.search(r'\[(.*)\]', info)
                resp_dict[index_for_mem_cache] = {
                    "mask": line.split("\n")[0],
                    "multiplier": int(info.split("= ")[1]),
                    "value": dec_to_bin(int(mem_number.group(1))),
                    "result": 0
                }
                index_for_mem_cache = index_for_mem_cache + 1

# print(resp_dict)

for element in resp_dict.keys():
    resp_dict[element]["value"] = str(resp_dict[element]["value"])
    while len(resp_dict[element]["value"]) != len(resp_dict[element]["mask"]):
        resp_dict[element]["value"] = "0" + resp_dict[element]["value"]

    result = ""
    for i in range(len(resp_dict[element]["value"])):
        if resp_dict[element]["mask"][i] == "X":
            result = result + "X"
        if resp_dict[element]["mask"][i] == "0":
            result = result + resp_dict[element]["value"][i]
        if resp_dict[element]["mask"][i] == "1":
            result = result + "1"

    resp_dict[element]['result'] = result

result = {}

for element in resp_dict.keys():
    posible_values = []
    indexes_of_x = ([m.start() for m in re.finditer('X', resp_dict[element]['result'])])
    resp_dict[element]['result'] = list(resp_dict[element]['result'])
    for i in range(pow(2, len(indexes_of_x))):
        decimal_value = str(dec_to_bin(i))
        while len(decimal_value) != len(indexes_of_x):
            decimal_value = "0" + decimal_value
        posible_values.append(list(decimal_value))

    for y in range(len(posible_values)):
        for index in range(len(posible_values[y])):
            resp_dict[element]['result'][indexes_of_x[index]] = posible_values[y][index]

        temp_value = int("".join(resp_dict[element]['result']), 2)
        result[temp_value] = resp_dict[element]['multiplier']

final_result = 0

for element in result.keys():
    final_result = final_result + int(result[element])

print(final_result)