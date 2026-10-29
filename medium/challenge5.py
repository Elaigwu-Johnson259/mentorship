def most_frequent(numbers):
    frequency = {}
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    most_frequent = max(frequency, key=frequency.get)
    return most_frequent

print(most_frequent([2, 5, 2, 8, 2, 5]))

