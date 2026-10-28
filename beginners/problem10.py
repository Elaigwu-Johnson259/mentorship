def move_zeros(numbers):
    zeros = 0
    seen = []
    for num in numbers:
        if num == 0:
            zeros += 1
            continue
        seen.append(num)
    seen.extend([0] * zeros)

    return seen


def move_zeros(numbers):
    zeros = []
    seen = []
    for num in numbers:
        if num == 0:
            zeros.append(num)
            continue
        seen.append(num)
    return seen + zeros 

print(move_zeros([0, 1, 0, 3, 12]))
print(move_zeros([1, 2, 3]))
print(move_zeros([0, 0, 5]))