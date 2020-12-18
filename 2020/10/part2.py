#!/usr/bin/python3

with open('./input.txt', 'r') as input:
    list_lines = input.read().split('\n')
    list_lines = [int(item) for item in list_lines]
    list_lines.sort()
    list_lines.append(list_lines[-1]+3)
    memo = {0: 1}
    for i in list_lines:
        memo[i] = memo.get(i-3,0) \
                + memo.get(i-2,0) \
                + memo.get(i-1,0)
    print(memo[list_lines[-1]])
    
input.close()