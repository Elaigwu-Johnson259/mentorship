def find_smallest(numbers):
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
            print(smallest)

find_smallest([8, 3, 12, 1, 7])
find_smallest([-3, -10, -1, -6])
