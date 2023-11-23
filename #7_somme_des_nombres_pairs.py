def sum_even_numbers(list):
    sum = 0
    for number in list:
        if number % 2 == 0:
            sum+= number
    return sum



numers_list = [1, 4, 6, 9, 45, 327, 18, 20]
result = sum_even_numbers(numers_list)
print(result)