#!/usr/bin/python3
import re, sys

count = 0

def translate_bag(single_bag, bags_list):
    translated_bag = []

    for bag in single_bag:
        for bag_from_list in bags_list:
            if bag == bag_from_list.split(" contain ")[0].replace(" bags", "").replace(" bag", ""):
                translated_bag.extend(re.sub('\d ', '', bag_from_list.split(" contain ")[1].replace(".", "").replace(" bags", "").replace(" bag", "")).split(", "))

    return translated_bag
    

with open('./input.txt', 'r') as input:
    bags_list = input.read().split('\n')
    for bag in bags_list:
        if ("no other" not in bag):
            bags_in_bag = re.sub('\d ', '', bag.split(" contain ")[1].replace(".", "").replace(" bags", "").replace(" bag", "")).split(", ")
            while True:
                if any(t == "shiny gold" for t in bags_in_bag):    
                    count += 1
                    break
                bags_in_bag = translate_bag(bags_in_bag, bags_list)
                if (bags_in_bag == []):
                    break
                
input.close()
print(count)