#!/usr/bin/python3

with open('./input.txt', 'r') as input:
    list_lines = input.read().splitlines()
    wrong_passwords = 0
    for line in list_lines:
        number_policy = line.split(" ")[0]
        letter_policy = line.split(" ")[1].replace(":", "")
        password = line.split(" ")[2]
        counted_apperances = password.count(letter_policy)

        start = int(number_policy.split("-")[0])-1
        stop = int(number_policy.split("-")[1])-1

        if password[start] != password[stop]:
            if password[start] == letter_policy or password[stop] == letter_policy:
                wrong_passwords += 1

    print(wrong_passwords)