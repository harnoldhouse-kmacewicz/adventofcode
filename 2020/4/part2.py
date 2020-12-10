#!/usr/bin/python3

import re

valid_passports = 0
with open('./input.txt', 'r') as input:
    list_lines = input.read().split('\n\n')
    required_in_passport = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    dict_passports = []
    for line in list_lines:
        passport = line.replace("\n", " ")
        if all(x in passport for x in required_in_passport):
            dict_passports.append(dict(data.split(':') for data in line.replace("\n", " ").split()))
        
    for passport in dict_passports:
        if len(passport['byr']) == 4 and int(passport['byr']) >= 1920 and int(passport['byr']) <= 2002:
            if len(passport['iyr']) == 4 and int(passport['iyr']) >= 2010 and int(passport['iyr']) <= 2020:
                if len(passport['eyr']) == 4 and int(passport['eyr']) >= 2020 and int(passport['eyr']) <= 2030:
                    if ('cm' in passport['hgt'] and int(passport['hgt'].replace("cm", "")) >= 150 and int(passport['hgt'].replace("cm", "")) <= 193) or ('in' in passport['hgt'] and int(passport['hgt'].replace("in", "")) >= 59 and int(passport['hgt'].replace("in", "")) <= 76):
                        if (re.match(r'#[\da-f]{6}', passport['hcl'])):
                            if (passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
                                if (re.match("^[0-9]{9}$", passport['pid'])):
                                    valid_passports += 1

print(valid_passports)
input.close()