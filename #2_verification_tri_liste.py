def is_list_sorted(list):
    for i in range(len(list)):
        if i + 1 < len(list):
            if list[i] > list[i + 1]:
                return False
    return True

numbers_list = [2, 5, 8, 13, 45, 56, 3]
result = is_list_sorted(numbers_list)
print(result)