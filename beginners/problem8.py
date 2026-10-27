# def has_duplicates(numbers):
#     duplicate = []
#     for number in numbers:
#        if number in duplicate:
#             return True
#         duplicate.add(number)
#     return False
# print(has_duplicates([1, 3, 2, 2]))
        
def has_duplicates(numbers):
    seen = set()

    for number in numbers:
        if number in seen:
            return True
        seen.add(number)
    return False
print(has_duplicates([1, 3, 2, 2]))