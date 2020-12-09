#!/usr/bin/python3

with open('./input.txt', 'r') as input:
    list_numbers = input.read().splitlines()
    list_numbers = [int(item) for item in list_numbers]
    for i in range(len(list_numbers)):
        for i_1 in range(i, len(list_numbers)):
            for i_2 in list_numbers[i_1:len(list_numbers)]:
                if list_numbers[i]+list_numbers[i_1]+i_2 == 2020:
                    print(list_numbers[i]*list_numbers[i_1]*i_2)