#!/usr/bin/python3

valid_passports = 0
with open('./input.txt', 'r') as input:
    list_lines = input.read().split('\n\n')
    required_in_passport = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for line in list_lines:
        passport = line.replace("\n", " ")
        if all(x in passport for x in required_in_passport):
            valid_passports += 1

    print(valid_passports)
input.close()