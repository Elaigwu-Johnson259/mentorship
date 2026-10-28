"""
def move_zeros(numbers):
    seen = []
    zeros = []
    for num in numbers:
        if num == 0:
            zeros.append(num)
            continue
        seen.append(num)

    return seen + zeros
"""

def move_zeros(numbers):
    seen = []
    zero_count = 0
    
    for number in numbers:
        
        if number == 0:
            zero_count += 1
            continue
            
        if number != 0:
            seen.append(number)
        seen.extend([0] * zero_count)
    return seen 

print(move_zeros([0, 1, 0, 3, 12]))
print(move_zeros([4, 0, 5, 0, 2]))
print(move_zeros([1, 2, 3]))