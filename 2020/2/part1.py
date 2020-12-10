#!/usr/bin/python3

with open('./input.txt', 'r') as input:
    list_lines = input.read().splitlines()
    wrong_passwords = 0
    for line in list_lines:
        number_policy = line.split(" ")[0]
        letter_policy = line.split(" ")[1].replace(":", "")
        password = line.split(" ")[2]
        counted_apperances = password.count(letter_policy)
        if int(number_policy.split("-")[0]) <= counted_apperances and counted_apperances <= int(number_policy.split("-")[1]):
            wrong_passwords += 1
    print(wrong_passwords)

input.close()