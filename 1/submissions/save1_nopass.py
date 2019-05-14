def sum_numbers(numbers=None):
    total = 0
    if numbers == None or numbers == 0:
        for num in (1, 101):
            total += num
            return total
    else:
        for num in numbers:
            total += num
            return total
        