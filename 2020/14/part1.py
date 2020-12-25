#!/usr/bin/python3

import re

resp_dict = {}

def dec_to_bin(x):
    return int(bin(x)[2:])

with open('./input.txt', 'r') as input:
    list_lines = input.read().split("mask = ")
    list_lines = "++".join(list_lines)
    list_lines = list_lines.split("++")
    list_lines = list(filter(None, list_lines))
    for line in list_lines:
        for info in line.split("\n")[1:]:
            if info != "":
                mem_number = re.search(r'\[(.*)\]', info)
                resp_dict[mem_number.group(1)] = {
                    "mask": line.split("\n")[0],
                    "value": dec_to_bin(int(info.split("= ")[1])),
                    "result": 0
                }

input.close()

for element in resp_dict.keys():
    resp_dict[element]["value"] = str(resp_dict[element]["value"])
    while len(resp_dict[element]["value"]) != len(resp_dict[element]["mask"]):
        resp_dict[element]["value"] = "0" + resp_dict[element]["value"]

    result = ""
    for i in range(len(resp_dict[element]["value"])):
        if resp_dict[element]["mask"][i] == "X":
            result = result + resp_dict[element]["value"][i]
        if resp_dict[element]["mask"][i] == "0":
            result = result + "0"
        if resp_dict[element]["mask"][i] == "1":
            result = result + "1"
            
    resp_dict[element]['result'] = int(result, 2)

final_result = 0

for element in resp_dict.keys():
    final_result = final_result + resp_dict[element]['result']

print(final_result)