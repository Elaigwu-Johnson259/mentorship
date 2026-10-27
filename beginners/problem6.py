def find_number(numbers, target):
    position = 0 
    total_numbers = len(numbers)
    while position < total_numbers:
        if numbers[position] == target:
            return position

        position += 1

    return -1



print(find_number([10, 25, 30, 45], 30))
print(find_number([5, 8, 5, 9], 5))
print(find_number([10, 20, 30], 99))

