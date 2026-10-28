def move_zeros(numbers):
    position = 0

    for i in range(len(numbers)):
        if numbers[i] != 0:
            numbers[position] = numbers[i]
            position += 1

    while position < len(numbers):
        numbers[position] = 0
        position += 1

numbers = [0, 1, 0, 3, 12]
move_zeros(numbers)
print(numbers)  # [1, 3, 12, 0, 0]

numbers = [4, 0, 5, 0, 2]
move_zeros(numbers)
print(numbers)  # [4, 5, 2, 0, 0]

numbers = [1, 2, 3]
move_zeros(numbers)
print(numbers)  # [1, 2, 3]
