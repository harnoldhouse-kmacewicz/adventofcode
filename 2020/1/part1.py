#!/usr/bin/python3

with open('./input.txt', 'r') as input:
    list_numbers = input.read().splitlines()
    list_numbers = [int(item) for item in list_numbers]
    for i in range(len(list_numbers)):
        for compare_number in list_numbers[i:len(list_numbers)]:
            if int(list_numbers[i]) + int(compare_number) == 2020:
                print(list_numbers[i]*compare_number)