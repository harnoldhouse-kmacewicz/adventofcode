#!/usr/bin/python3

count = 0

with open('./input.txt', 'r') as input:
    list_lines = input.read().split('\n\n')
    for line in list_lines:
        count += len({i:line.replace("\n", "").count(i) for i in line.replace("\n", "")})
        
    print(count)
input.close()