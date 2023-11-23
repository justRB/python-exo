def list_median(list):
    list.sort()
    print(list)
    lenght = len(list)
    if lenght % 2 != 0:
        return list[int(lenght / 2)]
    else :
        return (list[int(lenght / 2) - 1] + list[int((lenght / 2))]) / 2


numbers_list = [2, 78, 21, 24, 12, 43]
result = list_median(numbers_list)
print(result)
