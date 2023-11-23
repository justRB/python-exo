def the_second_largest_number(list):
    if len(list) < 2:
        return None
    firstLargestNumber = max(list)
    list.remove(firstLargestNumber)
    return max(list)


numbers_list = [4, 45, 36, 12, 27, 12, 14, 28, 11]
result = the_second_largest_number(numbers_list)
print(result)