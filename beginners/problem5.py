def count_occurrences(numbers, target):
    count = 0
    for number in numbers:
        if number == target:
            count += 1
    return count

print(count_occurrences([2, 5, 63, 2], 2))
