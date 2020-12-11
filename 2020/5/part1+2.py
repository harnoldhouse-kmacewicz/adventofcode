#!/usr/bin/python3

#!/usr/bin/python3

valid_passports = 0

def sort_list(list_to_sort):
    return list_to_sort.sort()

with open('./input.txt', 'r') as input:
    list_lines = input.read().splitlines()
    list_result = []

    for plane_row in list_lines:
        binary_row = plane_row.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1")
        list_result.append(int(binary_row, 2))

    print(max(list_result))

    previous_number = 0
    
    for seat_number in sorted(list_result):
        current_number = seat_number
        if (current_number != previous_number + 1 and previous_number != 0):
            print(previous_number + 1)
        previous_number = seat_number
        
input.close()
