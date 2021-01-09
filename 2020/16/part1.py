#!/usr/bin/python3

with open('./input.txt', 'r') as input:
    lines = input.read()
input.close()

lines = lines.split("\n\n")

rules = lines[0].split("\n")

rule_list = []

for rule in rules:
    resp_dict = {}
    for parsed_rule in rule.split(": ")[1].split(" or "):
        rule_list.append({'start': int(parsed_rule.split("-")[0]), 'stop': int(parsed_rule.split("-")[1])})

values = lines[2].replace("\n",",").split(",")[1:]
values = filter(bool, values)

ticket_error_count = 0

for value in values:
    value_found = True
    for rule in rule_list:
        if rule['start'] <= int(value) <= rule['stop']:
            value_found = False
    if value_found:
        ticket_error_count = ticket_error_count + int(value)

print(ticket_error_count)
