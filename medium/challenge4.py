def reverse_first(queue, k):
    reverse_part = queue[:k][::-1]
    remaining_part = queue[k:]

    return reverse_part + remaining_part

print(reverse_first([10, 20, 30, 40, 50], 3))
print(reverse_first([1, 2, 3, 4], 2))
