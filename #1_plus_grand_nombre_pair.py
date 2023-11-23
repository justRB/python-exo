def largest_even_number(list):
    event_number = [x for x in list if x % 2 == 0]
    if len(event_number) == 0 :
        return None
    return max(event_number)


numbers_list = [4, 45, 21, 56, 25, 12, 47, 18, 33, 16, 7]
result = largest_even_number(numbers_list)
print(result)