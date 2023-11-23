def sort_insertion(list):
    for i in range(1, len(list)):
        valueToInsert = list[i]
        
        y = i - 1
        while y >= 0 and valueToInsert < list[y]:
            list[y + 1] = list[y]
            y -= 1
        
        list[y + 1] = valueToInsert
    
    return list

list = [8, 2, 17, 12, 5, 36]
result = sort_insertion(list)
print(result)
