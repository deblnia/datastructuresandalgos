def sum_possible(amount, numbers):
    # the brute force way to solve 
    if amount == 0:
        return True 
    elif amount < 0:
        return False 
    for num in numbers: 
        if sum_possible(amount - num, numbers):
            return True 
    return False