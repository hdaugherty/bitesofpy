def sum_numbers(n=None):
    total = 0
    if n == None or n == 0:
        for num in range(1, 101):
            total += num
            return total
            
    else:
        for num in n:
            total += num
            return total