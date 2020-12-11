#!/usr/bin/python3

count = 0

with open('./input.txt', 'r') as input:
    for line in input.read().split('\n\n'):
        number_of_person_in_group = len(line.split("\n"))
        line_no_new_line = line.replace("\n", "")
        dict_with_questions = {i:line_no_new_line.count(i) for i in line_no_new_line}
        for question in dict_with_questions:
            if dict_with_questions[question] == number_of_person_in_group:
                count += 1
        
    print(count)
input.close()