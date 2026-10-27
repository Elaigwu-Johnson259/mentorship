def list_sum(numbers):
    if numbers == []:
        return "none"
    
    total = 0
    
    for number in numbers:
        total = total + number
        
        print(total)

list_sum([2, 4, 6, 8])
list_sum([-5, 10, -2])
list_sum([])