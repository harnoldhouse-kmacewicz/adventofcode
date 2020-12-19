#!/usr/bin/python3

matrix = []
matrix_before = []

def Cloning(li1): 
    li_copy = []
    for list_inside in li1:
        li_copy.append(list_inside[:])
    return li_copy 

with open('./input.txt', 'r') as input:
    list_lines = input.read().split('\n')
    for i in list_lines:
        matrix.append(list(i))
        matrix_before.append(list(i))
input.close()

for row in range(len(matrix)):
    if not any(x == "#" for x in matrix[row]):
        for column in range(len(matrix[row])):
            matrix[row][column] = matrix[row][column].replace("L", "#")
            matrix_before[row][column] = matrix_before[row][column].replace("L", "#")


while True:
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if matrix_before[row][column] == "L":
                if row - 1 >= 0:
                    if column -1 >= 0:
                        if matrix_before[row-1][column-1] == "#":
                            continue
                    if matrix_before[row-1][column] == "#":
                        continue
                    if len(matrix_before[row]) -2 -column >= 0:
                        if matrix_before[row-1][column+1] == "#":
                            continue

                if column -1 >= 0:
                    if matrix_before[row][column-1] == "#":
                        continue
                if len(matrix_before[row]) -2 -column >= 0:
                    if matrix_before[row][column+1] == "#":
                        continue

                if len(matrix) -2 -row >= 0:
                    if column -1 >= 0:
                        if matrix_before[row+1][column-1] == "#":
                            continue
                    if matrix_before[row+1][column] == "#":
                        continue
                    if len(matrix_before[row]) -2 -column >= 0:
                        if matrix_before[row+1][column+1] == "#":
                            continue

                matrix[row][column] = "#"


            if matrix_before[row][column] == "#":
                count = 0
                if row -1 >= 0:
                    if column -1 >= 0:
                        if matrix_before[row-1][column-1] == "#":
                            count += 1
                    if matrix_before[row-1][column] == "#":
                        count += 1
                    if len(matrix_before[row]) -2 -column >= 0:
                        if matrix_before[row-1][column+1] == "#":
                            count += 1
                
                if column -1 >= 0:
                    if matrix_before[row][column-1] == "#":
                        count += 1
                if len(matrix_before[row]) -2 -column >= 0:
                    if matrix_before[row][column+1] == "#":
                        count += 1

                if len(matrix) -2 -row >= 0:
                    if column -1 >= 0:
                        if matrix_before[row+1][column-1] == "#":
                            count += 1
                    if matrix_before[row+1][column] == "#":
                        count += 1
                    if len(matrix_before[row]) -2 -column >= 0:
                        if matrix_before[row+1][column+1] == "#":
                            count += 1
                
                if count >= 5:
                    matrix[row][column] = "L"

    if matrix == matrix_before:
        count_occupied = 0
        for row in range(len(matrix)):
            for column in range(len(matrix[row])):
                if matrix[row][column] == "#":
                    count_occupied += 1
        print(count_occupied)
        break

    matrix_before = Cloning(matrix)