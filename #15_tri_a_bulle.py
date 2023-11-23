def sort_bubble(list):
    for x in range(len(list)):
        for y in range(len(list)):
            try:
                left = list[y]
                right = list[y + 1]
                if left > right:
                    list[y] = right
                    list[y + 1] = left
            except:
                continue
    return list
    
result = sort_bubble([9, 7, 3, 14, 2, 45, 8, 1, 18, 4, 11])
print(result)