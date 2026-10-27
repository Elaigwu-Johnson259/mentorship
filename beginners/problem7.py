"""
def reverse_list(items):
    new_list = []
    reversed_items = reversed(items)
    for item in reversed_items:
        new_list.append(item)
    print(new_list)

"""
#reverse_list([1, 2, 3, 4])



def reverse_list(items):
    position = len(items) -1
    new_list = []
    
    while position >= 0:
        new_list.append(items[position]) 
        
        position -= 1
    
    return new_list

print(reverse_list([1, 2, 3, 4]))



