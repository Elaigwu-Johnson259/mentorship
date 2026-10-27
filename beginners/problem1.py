"""
def find_largest(numbers):
    if numbers == []:
        return None
    largest = numbers[0]
    try:
        for number in numbers:
            if number < largest:
                largest = number
                print(largest)
            if not isinstance(number, int):
                print("Program allows only digit")
            elif isinstance(number, bool):
                print("Program allows only digit")

    except ValueError:
        print("only integers is allowed")
    
find_largest(["3, 41, 56, 21, 76, 9"])
find_largest([-10, -5, -2, -18])
find_largest([True, False])
find_largest([])
"""

def find_largest(numbers):
    if numbers == []:
        return None
    
    largest = numbers[0]
    for num in numbers:
        
        if num > largest:
            largest = num
    
    return largest

print(find_largest([3, 41, 56, 21, 76, 9]))