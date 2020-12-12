#!/usr/bin/python3

import re
from collections import defaultdict

with open('./input.txt', 'r') as input:
    lines = input.read().split('\n')
    bags = defaultdict(dict)
    for l in lines:
        bag = re.match(r'(.*) bags contain', l).groups()[0]
        for count, b in re.findall(r'(\d+) (\w+ \w+) bag', l):
            bags[bag][b] = int(count)

def search(bag):
    count = 1
    for s in bags[bag]:
        multiplier = bags[bag][s]
        count += multiplier * search(s)
    return count

print(search('shiny gold') - 1)
